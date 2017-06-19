# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	#ninja got passed in through the url parameter!
	return render(request, 'ninjas/index.html')
def show(request, ninja_color):
    if ninja_color == "red":
        context = {
            'ninja_color': '../../static/ninjas/images/leonardo.jpg'
        }
    return render(request, 'ninjas/result.html',context)
    