# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length = 50)
    