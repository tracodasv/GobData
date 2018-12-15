from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'Solicitudes/index.html',{}) 


def nuevaSolicitud(request):
    return render(request,'')