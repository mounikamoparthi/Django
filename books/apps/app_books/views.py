# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from .models import Books

def index(request):
    Books.objects.create(title = " grokking algorithms", author = "AdityaY.Bhargava", category = "learners")
    book = Books.object.all()
    print book
    return render (request,'app_books/index.html')