from django.conf.urls import include, url
from . import views


urlpatterns = [  
	url(r'^registro/', views.registro, name='registro'),
	url(r'^recuperacion/', views.recuperacion, name='recuperacion'),  	
	#url(r'^$', views.index,name='index'),
	url('',views.index,name='index'),
	]
