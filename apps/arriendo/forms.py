from django import forms
from .models import Zona


class AgregarForm(forms.ModelForm):
	class Meta:
		model = Zona
		fields =[
			'nombre',    
            'direccion',
            'capacidad',
            'stock',
		]

		labels ={
            'nombre':'Nombre',    
            'direccion':'Direccion',
            'capacidad':'Capacidad',
            'stock':'Stock',
		}
		widgets ={
            'nombre':forms.TextInput(),
            'direccion':forms.TextInput(),
            'capacidad':forms.TextInput(),
            'stock':forms.TextInput(),
		}

class ModificarForm(forms.ModelForm):
	class Meta:
		model = Zona
		fields =[
			'nombre',    
            'direccion',
            'capacidad',
            'stock',
		]

		labels ={
            'nombre':'Nombre',    
            'direccion':'Direccion',
            'capacidad':'Capacidad',
            'stock':'Stock',
		}
		widgets ={
            'nombre':forms.TextInput(),
            'direccion':forms.TextInput(),
            'capacidad':forms.TextInput(),
            'stock':forms.TextInput(),
		}

class ConsultarForm(forms.ModelForm):
    class Meta:
        model = Zona
        fields=[
            'nombre',
        ]

        label ={
            'nombre': 'Nombre',
        }
        widgets ={
            'nombre':forms.TextInput(),
        }