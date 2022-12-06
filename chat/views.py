from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    return render(request, 'chat/index.html')


def room(request,room_name):
    return render(request,'chat/room.html',{'room_name':room_name})