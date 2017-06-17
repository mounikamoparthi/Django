# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse

def index(request):
    return render(request,'takesurvey/index.html')
def create(request):
    if request.method == "POST":
        print '********'
        print request.POST
        request.session['Name'] = request.POST['name']
        request.session['Location'] = request.POST['location']
        request.session['Language'] = request.POST['language']
        request.session['Comments'] = request.POST['comments']
        return redirect('/result')
    
def result(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
        request.session['counter'] = 1
    if request.method == "POST":
        return redirect('/')
    return render(request,'takesurvey/result.html')
