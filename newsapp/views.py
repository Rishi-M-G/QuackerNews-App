from django.shortcuts import render
# ***********************Delete this later*******************************
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, NewsInput,InviteFriendsForm
from django.contrib import messages
import requests
from django.core.mail import send_mail


# ***********************************************************************
# Create your views here.
# ***********************Delete this later*******************************
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
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled newsapp')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'newsapp/login.html', {'form': form})


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
        return render(request, 'newsapp/dashboard.html', context)
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        context = {
            'articles': articles
        }
        return render(request, 'newsapp/dashboard.html', context)


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
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, 'Error Updating your Profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'newsapp/edit.html', {'user_form': user_form, 'profile_form': profile_form})


def landing(request):
    return (request, 'index.html')

# def invite_friends(request):
#     sent = False
#     if request.method == 'POST':
#         form = InviteFriendsForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             link = f'https://quacker.com:8000/newsapp/login/'
#             subject = f"{cd['first_name']} invites you to Quacker"
#             message = f"Quacker is a web-based news application that feeds users the trending news in the locality of their choice using News API. Login here {link}"
#             send_mail(subject,message,'quacker.blackshark@gmail.com',[cd['to']])
#             sent = True
#         else:
#             form = InviteFriendsForm()
#         return render()


# ***********************************************************************

# def news(request):
#
#     if request.method == 'POST':
#         form = NewsInput(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             # url = f'https://newsapi.org/v2/everything?q=tesla&country={country}&apiKey={API_KEY}'
#             url = f'https://newsapi.org/v2/everything?q={cd}&apiKey={API_KEY}'
#             response = requests.get(url)
#             data = response.json()
#             articles = data['articles']
#             context = {
#                 'articles': articles
#             }
#     return render(request, 'newsapp/dashboard.html', context)
