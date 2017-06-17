# -*- coding: utf-8 -*-
#rom __future__ import unicode_literals

from django.shortcuts import render,redirect
import random
import string

def index(request):
    return render(request, 'generateword/index.html')
def create(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
        request.session['counter'] = 1
    word = ''
    for n in xrange(0,14):
        word = word + str(random.choice(string.ascii_letters + string.digits))
    words = {
        'random_word':word
    }
    print word
    return render(request, 'generateword/index.html',words)
   
