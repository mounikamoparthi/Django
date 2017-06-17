# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
def index(request):
    context ={
        "name":"Mounika"
    }
    return render(request, 'portfolio_app/index.html', context)
def projects(request):
    return render(request, 'portfolio_app/projects.html')
def about(request):
    return render(request, 'portfolio_app/about.html')
def testimonials(request):
    return render(request, 'portfolio_app/testimonials.html')


