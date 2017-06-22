# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
def index(request):
    print User.objects.all().delete()
    context = {
        'users' :  User.objects.all()
    }
    return render(request,'app_wall/index.html', context)

def registration(request):
    result = User.objects.register(request.POST)
    if not result['status']:
        for error in result['errors']:
            messages.error(request,error)
    else:
        messages.success(request,"Successful")
    return redirect('/')

def loginuser(request):
    return render(request,'app_wall/index.html')

