 
from django.shortcuts import render, HttpResponse,redirect
  # the index function is called when root is visited
def index(request):
  context = {
      "name ":"Mounika"
    }
  return render(request, 'quotes_app/index.html',context)