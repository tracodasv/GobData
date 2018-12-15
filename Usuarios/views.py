from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .forms import PersonaForm  
import pdb


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


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect ('solicitudes:index')
        else:
            return render(request,'Usuarios/login.html',{'error':'Usuario o contrasena invalidoS'})
    return render(request,'Usuarios/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        primerNombre = request.POST['primerNombre']
        segundoNombre = request.POST['segundoNombre']
        primerApellido = request.POST['primerApellido']
        segundoApellido = request.POST['segundoApellido']
        nombreCompleto = ''+primerNombre+" "+segundoNombre+" "+primerApellido+" "+segundoApellido
        documento = request.POST['documento']

    return render(request,"Usuarios/signup.html")

def datos(request):
    return render(request)