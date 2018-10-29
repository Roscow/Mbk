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
			'usuario',
			'contraseña',
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
			'usuario': 'Usuario',
			'contraseña': 'Contraseña',
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
			'usuario': forms.TextInput(),
			'contraseña': forms.TextInput(),
		}
		
class RecuperarForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields =[
			'correo',
		]

		labels ={
            'correo':'Ingrese su correo registrado para recibir su contraseña',
		}
        	  
		 
