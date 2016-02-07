from django.conf.urls import include, url, patterns
import views
from .viewsets import *
from rest_framework.routers import DefaultRouter
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
	url(r'^eventos/$', views.evento_nueva, name='evento_nueva'),
	url(r'^noticias/$', views.noticia_nueva, name='noticia_nueva'),

	url(r'^eventos/list$', views.evento_list, name='evento_list'),
	url(r'^eventos/(?P<pk>[0-9]+)/$', views.evento_detail, name='evento_detail'),

	url(r'^noticias/list$', views.noticia_list, name='noticia_list'),
	url(r'^noticias/(?P<pk>[0-9]+)/$', views.noticia_detail, name='noticia_detail'),


	url(r'^eventos/(?P<pk>[0-9]+)/edit/$', views.evento_edit, name='evento_edit'),
	url(r'^noticias/(?P<pk>[0-9]+)/edit/$', views.noticia_edit, name='noticia_edit'),
	


    url(r'^list$', views.list),
    # URL for uploading an image
    url(r'^upload$', views.upload),
    # The direct upload functionality reports to this URL when an image is uploaded.
    url(r'^upload/complete$', views.direct_upload_complete),




]