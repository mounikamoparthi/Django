# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product
def index(request):
    Product.objects.create(name="Michael choi",description="Hiall",weight = 4,Price= 20,Cost_to_seller= 19,category='vegetable')
    output = Product.objects.filter(id =1)
     
    product1 = Product.objects.all()
    for pp in product1:
        print pp.name,pp.description,pp.weight,pp.Cost_to_seller,pp.Price,pp.category
    print product1
    print output 
    return render(request, 'app_product/index.html')