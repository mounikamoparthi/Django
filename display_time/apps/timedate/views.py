# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'time': 'datetime.now()'
    }
    return render(request, 'timedate/index.html',context)