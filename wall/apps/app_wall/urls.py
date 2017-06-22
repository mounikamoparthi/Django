from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.add_users),
    url(r'^loginpage$', views.userlogin),
    url(r'^wall$', views.wallpage) # This line has changed!
  ]