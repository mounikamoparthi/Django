# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request,'app_landscape/index.html') 
def showimg(request,num):
    context = {
        'number' : int(num)
    }
    return render(request,'app_landscape/showimg.html', context)