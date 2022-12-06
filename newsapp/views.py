import random
import requests
import django
import channels
import social_django

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm  # UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, News, Articles,Rating
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, InviteForm
from django.contrib import messages
from random import shuffle
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Contact
from common.decorators import ajax_required
from django.db import connection
import inspect
from django.test import TestCase

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated ' \
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'newsapp/login.html', {'form': form})

def landing(request):
    return render(request, 'newsapp/index.html')

@login_required
def dashboard(request):
    API_KEY = '4205006ffd1f42c29743498f9255c2f8'
    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        context = {
            'articles': articles
        }
        save_news_general(data)
        return render(request, 'newsapp/dashboard.html', context)
    elif request.GET.get('category'):
        category = request.GET.get('category')
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        context = {
            'articles': articles
        }
        save_news_general(data)
        return render(request, 'newsapp/dashboard.html', context)
    elif request.GET.get('country'):
        country = request.GET.get('country')
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        context = {
            'articles': articles
        }
        save_news_general(data)
        return render(request, 'newsapp/dashboard.html', context)
    else:
        # if Profile.DoesNotExist:
        #     url = f'https://newsapi.org/v2/top-headlines?country=ca&apiKey={API_KEY}'
        #     response = requests.get(url)
        #     data = response.json()
        #     articles = data['articles']
        #     context = {
        #         'articles': articles
        #     }
        #     return render(request, 'newsapp/dashboard.html', context)
        # else:
        keyword1 = request.user.profile.category_pref1
        keyword2 = request.user.profile.category_pref2
        keyword3 = request.user.profile.category_pref3
        url1 = f'https://newsapi.org/v2/everything?q={keyword1}&apiKey={API_KEY}&pageSize=15'
        url2 = f'https://newsapi.org/v2/everything?q={keyword2}&apiKey={API_KEY}&pageSize=15'
        url3 = f'https://newsapi.org/v2/everything?q={keyword3}&apiKey={API_KEY}&pageSize=15'
        response1 = requests.get(url1)
        response2 = requests.get(url2)
        response3 = requests.get(url3)
        data1 = response1.json()
        data2 = response2.json()
        data3 = response3.json()
        save_news_general(data1)
        save_news_general(data2)
        save_news_general(data3)
        articles = data1['articles'] + data2['articles'] + data3['articles']
        context = {
            'articles': articles
        }
        return render(request, 'newsapp/dashboard.html', context)

def trending(request):
    API_KEY = '4205006ffd1f42c29743498f9255c2f8'
    if request.GET.get('country'):
        country = request.GET.get('country')
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        context = {
            'articles': articles
        }
        return render(request, 'newsapp/trending.html', context)
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=ca&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        context = {
            'articles': articles
        }
        return render(request, 'newsapp/trending.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # create user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'newsapp/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'newsapp/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'newsapp/edit.html', {'user_form': user_form, 'profile_form': profile_form})


def invite_friends(request):
    sent = False
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            url = 'https://quacker.com:8000/newsapp/login'
            subject = f"{cd['name']} recommends you to Signup for Quacker"
            message = f"Sign Up with Quacker at {url}"
            send_mail(subject, message, 'quacker.blackshark@gmail.com', [cd['to_email']])
            sent = True
    else:
        form = InviteForm()
    return render(request, 'newsapp/invite_friends.html', {'form': form, 'sent': sent})


# FOR FOLLOW FUNCTIONALITY
@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)

    return render(request, 'newsapp/user/list.html', {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    API_KEY = '4205006ffd1f42c29743498f9255c2f8'
    user = get_object_or_404(User, username=username, is_active=True)
    keyword1 = user.profile.category_pref1
    keyword2 = user.profile.category_pref2
    keyword3 = user.profile.category_pref3
    url1 = f'https://newsapi.org/v2/everything?q={keyword1}&apiKey={API_KEY}&pageSize=5'
    url2 = f'https://newsapi.org/v2/everything?q={keyword2}&apiKey={API_KEY}&pageSize=5'
    url3 = f'https://newsapi.org/v2/everything?q={keyword3}&apiKey={API_KEY}&pageSize=5'
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    data1 = response1.json()
    data2 = response2.json()
    data3 = response3.json()
    articles = data1['articles'] + data2['articles'] + data3['articles']
    return render(request, 'newsapp/user/detail.html', {'section': 'people', 'user': user,'articles':articles})


# @ajax_required
# @require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from=request.user,
                    user_to=user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})


def save_news_general(data):
    for item in data['articles']:
        Articles.objects.create(title=item['title'],
                                author=item['author'],
                                description=item['description'],
                                url=item['url'],
                                url_to_image=item['urlToImage'],
                                published_at=item['publishedAt'])

print("****** INSPECTION ******")
print("\n")
print("-----Inspection of Classes-----")
print("\n")
print("User Class: ",inspect.isclass(User))
print("Profile Class: ",inspect.isclass(Profile))
print("Article Class: ",inspect.isclass(Articles))
print("Contact Class: ",inspect.isclass(Contact))
print("Rating Class: ",inspect.isclass(Rating))
print("\n")
print("-----Inspection of Imported Modules-----")
print("\n")
print("Django Module: ",inspect.ismodule(django))
print("Channels Module: ",inspect.ismodule(channels))
print("Social Authentication Module: ",inspect.ismodule(social_django))
print("\n")
print("-----Inspection of Functions-----")
print("\n")
print("Landing View: ",inspect.isfunction(landing))
print("User Login View: ",inspect.isfunction(user_login))
print("Dashboard View: ",inspect.isfunction(dashboard))
print("Trending View: ",inspect.isfunction(trending))
print("Register View: ",inspect.isfunction(register))
print("Edit View: ",inspect.isfunction(edit))
print("Invite Friends View: ",inspect.isfunction(invite_friends))
print("Followers List View: ",inspect.isfunction(user_list))
print("Followers Detail View: ",inspect.isfunction(user_detail))
print("Follow Request: ",inspect.isfunction(user_follow))
print("Save News: ",inspect.isfunction(save_news_general))
print("\n")
def detail(request, title):
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM dbo.newsapp_articles WHERE title= %s", [title])
    #     article = cursor.fetchone()
    #     print(article)
    article = Articles.objects.filter(id=14217)
    return render(request, 'newsapp/detail.html', {'article': article})

    # for item in Articles.objects.values_list('title', flat=True).distinct():
    #     Articles.objects.filter(pk__in=Articles.objects.filter(title=item).values_list('title', flat=True)[1:]).delete()

# def submit_rating(request,title):
#     if request.method == 'POST':
#         try


# def save_news_user(request,title):
#     user_id = request.POST.get('id')
#     action = request.POST.get('action')
#     article = Articles.objects.get(title=title)
#     user = User.objects.get('id')
#     if action=='save':
#         News.objects.create()
