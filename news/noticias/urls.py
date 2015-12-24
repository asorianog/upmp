from django.conf.urls import include, url
import views
from .viewsets import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
	url(r'^eventos$', views.evento_nueva, name='evento_nueva'),
	url(r'^noticias$', views.noticia_nueva, name='noticia_nueva'),
	url(r'^eventos/(?P<pk>[0-9]+)/edit/$', views.evento_edit, name='evento_edit'),
	#url(r'^noticias/(?P<pk>[0-9]+)/edit/$', views.noticia_edit, name='noticia_edit'),


]