from django.conf.urls import include, url
from . import views


urlpatterns = [   
	url(r'^agregar/', views.agregar, name='agregar'),  
	url(r'^listar/', views.listar, name='listar'),  
	url(r'^consultar/', views.consultar, name='consultar'),  
	]
