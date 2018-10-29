from django.shortcuts import render , redirect 
from .forms import RegistroForm


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



	
def index(request):
    return render(request, 'templates/index.html', {})
