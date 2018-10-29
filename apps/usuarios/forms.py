from django import forms
from .models import Usuario
from .models import Cuenta

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =[
            'run',
	        'nombre' ,
	        'apellido' ,
	        'correo' ,
	        'fecha_nacimiento',
	        'telefono',
	        'region' ,
	        'comunaDomicilio' ,
	        'comunaTrabajo' ,
        ]

        labels ={
            'run':'Rut',
	        'nombre':'Nombre' ,
	        'apellido':'Apellido' ,
	        'correo':'Correo Electronico' ,
	        'fecha_nacimiento':'Fecha de nacimiento',
	        'telefono':'Telefono',
	        'region' :'Region',
	        'comunaDomicilio':'Comuna de domicilio' ,
	        'comunaTrabajo':'No vivo en la comuna pero trabajo en ella' ,
		}

        widgets ={
            'run':forms.TextInput(),
	        'nombre': forms.TextInput(),
	        'apellido':forms.TextInput() ,
	        'correo':forms.TextInput() ,
	        'fecha_nacimiento': forms.SelectDateWidget(),
	        'telefono': forms.TextInput(),
	        'region' : forms.TextInput(),
	        'comunaDomicilio': forms.TextInput(),
	        'comunaTrabajo': forms.CheckboxInput(),
		}