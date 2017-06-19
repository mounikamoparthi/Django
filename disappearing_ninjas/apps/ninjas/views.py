# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	#ninja got passed in through the url parameter!
	return render(request, 'ninjas/index.html')

def showall(request):
    if  ninja_color is None:
        context = {
            'red': '../static/ninjas/images/raphael.jpg',
            'blue': '../static/ninjas/images/leonardo.jpg',
            'purple': '../static/ninjas/images/donatello.jpg',
            'orange': '../static/ninjas/images/michelangelo.jpg'
        }
    return render(request, 'ninjas/showall.html',context)

def show(request, ninja_color):
    if ninja_color == "red" or ninja_color is None:
        context = {
            'ninja_color': '../static/ninjas/images/raphael.jpg'
        }
   
    if ninja_color == "blue" or ninja_color is None:
        context = {
            'ninja_color': '../static/ninjas/images/leonardo.jpg'
        }
   
    if ninja_color == "purple" or ninja_color is None:
        context = {
            'ninja_color': '../static/ninjas/images/donatello.jpg'
        }
    if ninja_color == "orange" or ninja_color is None:
        context = {
            'ninja_color': '../static/ninjas/images/michelangelo.jpg'
        }
    if ninja_color != 'red' and ninja_color !='blue' and ninja_color !='orange' and ninja_color !='purple':
        context = {
            'ninja_color': '../static/ninjas/images/notapril.jpg'
        }
    return render(request, 'ninjas/result.html',context)
    