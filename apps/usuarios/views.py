from django.shortcuts import render , redirect 
from .forms import RegistroForm , RecuperarForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            Usuario = form.save(commit=True)
            Usuario.save()
            return redirect('/admin/ ')
    else:
        form = RegistroForm()
    return render(request, 'templates/registro.html', {'form': form} )

def recuperacion(request):
    if request.method == 'POST':
        form = RecuperarForm(request.POST)
        if form.is_valid():                       
            return redirect('/admin/ ')
    else:
        form = RecuperarForm()
    return render(request, 'templates/recuperar.html', {'form': form} )


	
def index(request):
    return render(request, 'templates/index.html', {})
