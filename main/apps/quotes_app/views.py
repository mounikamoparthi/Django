 
from django.shortcuts import render, HttpResponse
  # the index function is called when root is visited
def index(request):
    print (request.method)
    response = "Hello, I am your first request!"
    return render(request, 'quotes_app/index.html')