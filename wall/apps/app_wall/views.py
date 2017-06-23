# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
def index(request):
    #print User.objects.all().delete()
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
    result = User.objects.loginval(request.POST)
    if not result['status']:
        for error in result['errors']:
            messages.error(request,error)
        return redirect('/')
    else:
        messages.success(request,"Successful")
        request.session['emailid'] = result['user'].emailid
        request.session['first_name'] = result['user'].first_name
        request.session['user_id'] = result['user'].id
        print result['user'].emailid
        return redirect('/wall')

def wallpage(request):
    print request.method
    if request.method == "POST":
        context ={
        "name": request.session['first_name'],
        "id" :request.session['user_id'] 
        }
        #user_id=int(id)
        user1 = User.objects.get(id = context['id'])
        print user1
        print request.POST
        if 'messages' in request.POST:
            Message.objects.create(message=request.POST['messages'],user1 = user1)
        return redirect('/wall')
    else:
        context = {
        'blog' :  Message.objects.all(),
        "name": request.session['first_name'],
        "id" :request.session['user_id']
        }
        return render(request,'app_wall/wall.html', context)


    
   




