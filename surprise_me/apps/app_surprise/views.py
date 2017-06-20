# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
import string
import random

VALUES = ["Stack", "Overflow", "rocks"]
def index(request):
    print request.POST
    
    return render (request, 'app_surprise/index.html')

def results(request):
    print(random.choice(VALUES))
    print request.POST
    str1=''
    for i in range(0,int(request.POST['RandomNum'])):
        str1 = str1+" "+random.choice(VALUES)+'\n'
    context = {
        'number' : str1 
    }
    return render (request, 'app_surprise/results.html',context)

