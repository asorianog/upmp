from django.conf.urls import include, url
import views
from .viewsets import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
	url(r'^post/new/$', views.post_new, name='post_new'),
]