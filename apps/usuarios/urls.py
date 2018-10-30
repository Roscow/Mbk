from django.conf.urls import include, url
from . import views


urlpatterns = [   
	
	url(r'^index/', views.index, name='index'),  
	
	url(r'^administrar/', views.administrar, name='administrar'),  	  	
	#url(r'^$', views.index,name='index'),
	#url('',views.index,name='index'),
	url(r'^administracion/', views.administracion, name='administracion'),	
	url(r'^login/', views.login, name='login'),	
	url(r'^registro/', views.registro, name='registro'),
	url(r'^recuperacion/', views.recuperacion, name='recuperacion'),
	url(r'^zonas/', views.zonas, name='zonas'), 
	]
