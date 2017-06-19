# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def show_ninja(request, ninja):
	#ninja got passed in through the url parameter!
	context = {
        'myninja' : ninja
        }
	return render(request, 'ninjas/showmyninja.html', context)
