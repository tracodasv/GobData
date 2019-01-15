import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Solicitud,DetalleSolicitud,Requerimiento
from Usuarios.models import Persona
from Alcaldias.models import Alcaldia,Municipio
from django.contrib.auth.models import User 
from Usuarios.forms import DocumentosForm
import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def home_view(request):
    return render(request,'home.html')
 

def solicitante(request):
    if request.method == 'POST':
        nombreCompleto = request.POST['solicitante']
        documento = request.POST['documento']
        genero = request.POST['genero']
        fechaNacimiento = request.POST['fechaNacimiento']
        email = request.POST['email']
        return redirect()

    return(request)


def nuevaSolicitud(request):
    context = {}
    solicitante = None
    if request.user.is_authenticated:
        try:
            solicitante = Persona.objects.get(usuario=User.objects.get(username=request.user.username))
        except Persona.DoesNotExist:
            solicitnte = None
            context = {
                'user': request.user
            }
        else:
            print(request.user) 
            
            context.update( { 'solicitante':solicitante,
                        'user':request.user} )

    if request.method == 'POST':
        requisito = request.POST['requisito']
        alcaldia = request.POST['alcaldia']
        requerimiento = Requerimiento(peticion=requisito,alcaldia=Alcaldia.objects.get(municipio=Municipio.objects.get(nombreMunicipio=alcaldia)))
        if solicitante:
            solicitud = Solicitud(solicitante = solicitante)
        else:
            solicitud = Solicitud()
        
        solicitud.save()
        noAuth = request.POST['solicitante']
        detalle = DetalleSolicitud(solicitud=solicitud,nombreSolicitante=noAuth)
        detalle.save()
        print(request.POST)
        requerimiento.detalleSolicitud = detalle
        requerimiento.save()
        if solicitante:
            if solicitante.firma:
                return redirect('solicitudes:doc',solicitud.pk)
            else:
                return redirect('solicitudes:docs',solicitud=solicitud.pk,detalle=detalle.pk)
        else:
            return redirect('solicitudes:docs',solicitud=solicitud.pk,detalle=detalle.pk)

    
    return render(request,'Solicitudes/index.html',context)


def recoleccion_de_documentos(request,solicitud,detalle):
    context = {}
    if request.user.is_authenticated :
        persona = Persona.objects.get(usuario=User.objects.get(username=request.user.username))
        context.update({'persona':persona})
    detalleActual = DetalleSolicitud.objects.get(pk=detalle) 
    form = DocumentosForm()
    solicitudActual = Solicitud.objects.get(pk=solicitud)
    if form.is_valid():
        form = form.cleaned_data
        detalleActual.firma = form.firma
        detalleActual.documentoAnterior = form.documentoFotoAnterior
        detalleActual.documentoPosterior = form.documentoFotoPosterior
        detalleActual.save()
        
        return redirect('solicitudes:doc',solicitudActual.pk)
    
    return render(request,'Usuarios/documentos.html',context)


def docGen(request,idSolicitud):
    solicitud = Solicitud.objects.get(pk=idSolicitud)
    detalle = DetalleSolicitud.objects.get(solicitud=solicitud)
    requerimiento = Requerimiento.objects.get(detalleSolicitud=detalle)
    introduccionln = '''En el ejercicio del derecho que me es reconocido en el artículo dos de la Ley de Acceso a la 
    Información Pública y que deriva del artículo seis de la Constitución de la República, a bien tengo
    requerir lo siguiente:'''
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename={}{}.pdf'.format(detalle.nombreSolicitante,datetime.datetime.now())

    buffer = BytesIO()
    c = canvas.Canvas(buffer,pagesize=A4)

    c.setLineWidth(.3)
    c.setFont('Helvetica',13)
    c.drawString(480,750,datetime.datetime.now().strftime('%d/%m/%y'))
    c.line(460,747,560,747)
    c.drawString(30,750,'Oficial de Informacion')
    c.setFont('Helvetica',10)
    c.drawString(30,735,introduccionln)

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
    

