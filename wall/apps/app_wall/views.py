# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User, Message, Comment
def index(request):
    context = {
        "users": User.objects.all(),
        "message11": Message.objects.all()
    }
    return render(request,'app_wall/index.html', context)

def add_users(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], emailid=request.POST['emailid'], password=request.POST['password'])
    return redirect('/')

def userlogin(request):
    return render(request,'app_wall/login.html')

def wallpage(request,id):
    user = User.objects.get(id = id)
    print request.POST
    if 'messages' in request.POST:
        Message.objects.create(messages=request.POST['messages'],user = user)
    return redirect('/')
    #return render(request,'app_wall/posts.html')

def loginUser(request):
    print request.POST['emailid']
    print request.POST['password']
    return render(request,'app_wall/posts.html')
