from django.conf.urls import url, include
# from django.contrib import admin
from . import views
urlpatterns = [
        url(r'^$', views.index),
        url(r'^link$', views.link_actors),
        url(r'^back$', views.index),



        ]
