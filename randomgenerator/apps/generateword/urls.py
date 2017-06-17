
from django.conf.urls import urlsfrom .import views
urlpatterns = [
    url(r'^$', views.index)
]