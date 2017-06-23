# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
def index(request):
    #User.objects.all().delete()
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
    #Message.objects.all().delete()
    if request.method == "POST":
        if request.POST['action'] == "postmsg":
            context = {
                "name": request.session['first_name'],
                "id" :request.session['user_id']
                }
            result = User.objects.addmsgs(request.POST,context)
            print request.method
            if not result['status']:
                for error in result['errors']:
                    messages.error(request,error)
                    return redirect('/wall')
            else: 
                messages.success(request,"Successful")
                return redirect('/wall')
        else:
            context = {
                "name": request.session['first_name'],
                "id" :request.session['user_id']
                }
            result = User.objects.addcomments(request.POST,context)
            print request.method
            if not result['status']:
                for error in result['errors']:
                    messages.error(request,error)
                    return redirect('/wall')
            else: 
                messages.success(request,"Successful")
                return redirect('/wall')

            print "DIDNT ENTER"
    else:
            print "ENTERED GET"
            context = {
                    'blog' :  Message.objects.all(),
                    "name": request.session['first_name'],
                    "usercomments" : Comment.objects.all()
                }
    return render(request,'app_wall/wall.html', context)




   




