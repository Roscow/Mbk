from django.shortcuts import render, redirect
from .forms import AgregarForm ,ConsultarForm
from .models import Zona 


def agregar(request):
    if request.method == 'POST':
        form = AgregarForm(request.POST)
        if form.is_valid():
            Zona = form.save(commit=True)
            Zona.save()
            return redirect('/admin/ ')
    else:
        form = AgregarForm()
    return render(request, 'templates/zonas/agregar.html', {'form': form} )


def listar(request):
    zonas = Zona.objects.filter()
    return render(request,'templates/zonas/listar.html', {'zonas': zonas})



def consultar(request):
    if request.method == 'POST':
        form = ConsultarForm(request.POST)
        if form.is_valid():
                       
            return redirect('/admin/ ')
    else:
        form = ConsultarForm()
    return render(request, 'templates/zonas/consultar.html', {'form': form} )
