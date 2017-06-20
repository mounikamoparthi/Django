# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=38)
    greeting = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)

