from django import forms
from .models import Usuario

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
	        'nombre':'cosa' ,
	        'apellido':'cosa' ,
	        'correo':'cosa' ,
	        'fecha_nacimiento':'cosa',
	        'telefono':'cosa',
	        'region' :'cosa',
	        'comunaDomicilio':'cosa' ,
	        'comunaTrabajo':'cosa' ,
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
	        'comunaTrabajo': forms.TextInput(),
		}