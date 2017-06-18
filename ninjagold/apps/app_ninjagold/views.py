# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render,redirect
import random
from datetime import datetime

def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    if 'activities_log' not in request.session:
        request.session['activities_log'] = []
    return render(request,'app_ninjagold/index.html')

def goldcoins(request):
    if request.method == "POST":
        print '********'
        print request.POST
        if request.POST['action'] == 'Farm':
            farm_add = random.randint(10,20)
            request.session['goldcoins'] += farm_add 
            print request.session
            string = "You have earned"+ " "+ str(farm_add) + " " +"gold coins from the farm" + str(datetime.now().strftime("%Y/%m/%d"))
            request.session['activities_log'].append(string)
            print farm_add
        elif request.POST['action'] == 'Cave':
            cave_add = random.randint(5,10)
            request.session['goldcoins'] += cave_add
            string = "You have earned"+" "+ str(cave_add) + " " +"gold coins from the farm" + str(datetime.now().strftime("%Y/%m/%d"))
            request.session['activities_log'].append(string)
            
        elif request.POST['action'] == 'House':
            house_add = random.randint(2,5)
            request.session['goldcoins'] += house_add
            string = "You have earned"+ " " +str(house_add) + " " +"gold coins from the farm" + str(datetime.now().strftime("%Y/%m/%d"))
            request.session['activities_log'].append(string)
            print house_add
        elif request.POST['action'] == 'Casino':
            Casino_add = random.randint(0,50)
            request.session['goldcoins'] += Casino_add
            string = "You have earned"+" "+ str(Casino_add) + " " +"gold coins from the farm" + str(datetime.now().strftime("%Y/%m/%d"))
            request.session['activities_log'].append(string)
           
        return redirect('/')
   

