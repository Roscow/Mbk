from django.db import models
from django.utils import timezone
# Create your models here.


class Usuario(models.Model):
	run = models.CharField(primary_key=True, max_length=50)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.EmailField(max_length=50)
	fecha_nacimiento = models.DateTimeField(blank=True, null=False)
	telefono = models.IntegerField()
	region = models.CharField(max_length=50)
	comunaDomicilio = models.CharField(max_length=50)
	comunaTrabajo = models.CharField(max_length=50)   
	usuario = models.CharField(null=True,max_length=50)
	contraseña = models.CharField(null=True, max_length=50)
     

	def publish(self):
                self.save()
        
	def __str__(self):
                return self.nombre + ' ' +self.apellido        
                   


class Cuenta(models.Model):	
	usuario = models.CharField(null=True,max_length=50)
	contraseña = models.CharField(null=True, max_length=50)
        
	def __str__(self):
                return self.usuario     
                   
