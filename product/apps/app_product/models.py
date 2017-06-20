# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=38)
    description = models.TextField()
    weight = models.IntegerField()
    Price = models.IntegerField()
    Cost_to_seller = models.IntegerField()
    category = models.CharField(max_length=38)
    

