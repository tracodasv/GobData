from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PersonaForm  

def index(request):
    return HttpResponse("Index")

def PersonaFormulario(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('solicitudes:index')
    else:
        form = PersonaForm()
    return render(request,'Usuarios/personaCrear.html',{'form':form})
