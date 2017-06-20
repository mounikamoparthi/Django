# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product
def index(request):
    Product.objects.create(name="Michael choi",description="Hiall",weight = 4,Price= 20,Cost_to_seller= 19,category='vegetable')
    product = Product.objects.all()
    print product
    return render(request, 'app_product/index.html')