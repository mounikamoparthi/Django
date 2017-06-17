# -*- coding: utf-8 -*-
#rom __future__ import unicode_literals

from django.shortcuts import render
import random
import string

def index(request):
    random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)])
    print random
    return render(request, 'generateword/index.html')
