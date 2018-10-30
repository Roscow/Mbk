from django.db import models
from django.utils import timezone
# Create your models here.




class Zona(models.Model):	
    nombre =models.CharField(primary_key=True, max_length=50)	    
    direccion =models.CharField(max_length=50)
    capacidad =models.CharField(max_length=50)
    stock =models.CharField(max_length=50)
    
	