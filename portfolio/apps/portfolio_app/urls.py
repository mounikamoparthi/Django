from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),url(r'^testimonials$', views.testimonials)    # This line has changed! function name views.index
  ]