from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index),
	url(r'^show/(?P<ninja_color>\w+)$', views.show)     # 'home' route.
]
 