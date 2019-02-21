from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .forms import PersonaForm, DocumentosForm
from .models import Persona



def datos(request):
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
            return redirect ('solicitudes:nuevaSolicitud')
        else:
            return render(request,'Usuarios/login.html',{   'error':'Usuario o contrasena invalidos',
                                                            'User':request.user.is_authenticated})
    return render(request,'Usuarios/login.html',{'User':request.user.is_authenticated})


def signup_view(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        passwordcon = request.POST['passwordcon']
        primerNombre = request.POST['primerNombre']
        segundoNombre = request.POST['segundoNombre']
        primerApellido = request.POST['primerApellido']
        segundoApellido = request.POST['segundoApellido']
        nombreCompleto = ''+primerNombre+" "+segundoNombre+" "+primerApellido+" "+segundoApellido
        documento = request.POST['documento']
        if password != passwordcon:
            return render(request,"Usuarios/signup.html",{'error':'Contrasenas no coinciden'})
        else:
            print(username)

            usuario = User.objects.create_user(username=username,password=password)
            usuario.save()
            print(usuario.pk)

            persona = Persona.objects.create(
                primerNombre=primerNombre,
                segundoNombre=segundoNombre,
                primerApellido=primerApellido,
                segundoApellido=segundoApellido,
                dui=documento,
                usuario=usuario)

            print(persona)
            persona.save()
            print(persona.pk)
            user = authenticate(request,username=username,password=password)
            login(request,user)
    return render(request,"Usuarios/signup.html")


def logout_func(request):
    logout(request)
    return redirect('usuarios:login')

def upload_Docs(request):
    context= {}
    if request.method == 'POST':
        form = DocumentosForm(request.POST,request.FILES)
        persona = Persona.objects.get(usuario=User.objects.get(username=request.user.username))
        if request.user.is_authenticated:
            context = {
                'user' : request.user,
                'persona' : persona,
                'form':form
            }
        else:
            context = {
                'persona':'',
                'form':form,
            }
        if form.is_valid():
            data = form.cleaned_data
            persona.firma = data['firma']
            persona.documentoFotoAnterior = data['documentoFotoAnterior']
            persona.documentoFotoPosterior = data['documentoFotoPosterior']
            persona.save()
            print (form.cleaned_data)
            return redirect('solicitudes:nuevaSolicitud')
    return render(request,'./Usuarios/documentos.html',context)
