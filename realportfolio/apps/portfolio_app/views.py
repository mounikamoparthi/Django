# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
def index(request):
    context ={
        "name":"name"
    }
    return render(request, 'portfolio_app/index.html', context)

# Create your views here.
