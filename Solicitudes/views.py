import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Solicitud,DetalleSolicitud,Requerimiento
from Usuarios.models import Persona
from Alcaldias.models import Alcaldia,Municipio
from django.contrib.auth.models import User
from Usuarios.forms import DocumentosForm
from .forms import MultiRequerimiento
import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from math import ceil

def home_view(request):
    return render(request,'home.html')

#Regresa una tupla con el texto nuevo y el numero de lineas
def acotarCadenas(texto="""""",maxCararcteres=100,variacion=10):
    totalCaracteres = len(texto)
    limMin = maxCararcteres - variacion
    limMax = maxCararcteres + variacion
    lineas = 1
    pocisionSalto = 0
    while limMax < totalCaracteres + maxCararcteres:
        if totalCaracteres>maxCararcteres:
            textoInicial = texto
            salto = texto[limMin:limMax]
            pocisionSalto = int(salto.find(' '))
            while pocisionSalto == -1:
                limMin = limMin - 5
                salto = texto[limMin:limMax]
                pocisionSalto = int(salto.find(' '))
                print(pocisionSalto)
            pocisionSalto = pocisionSalto + int(limMin)
            texto = texto[:pocisionSalto]+'''
            '''+texto[pocisionSalto+1:]
            limMin = limMin + maxCararcteres
            limMax = limMin + variacion
            lineas = lineas + 1
        resultado = (texto,lineas)
    return resultado


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
    detalleActual = DetalleSolicitud.objects.get(pk=detalle)

    if request.method == 'POST':
        form = DocumentosForm(request.POST,request.FILES)

        solicitudActual = Solicitud.objects.get(pk=solicitud)
        if request.user.is_authenticated :
            persona = Persona.objects.get(usuario=User.objects.get(username=request.user.username))
            context.update({'persona':persona})

        if form.is_valid():
            form = form.cleaned_data
            detalleActual.fotoFirma = form['firma']
            detalleActual.documentoAnterior = form['documentoFotoAnterior']
            detalleActual.documentoPosterior = form['documentoFotoPosterior']
            detalleActual.save()
            print (form)
            return redirect('solicitudes:doc',solicitudActual.pk)


    return render(request,'Usuarios/documentos.html',context)


def docGen(request,idSolicitud):
    solicitud = Solicitud.objects.get(pk=idSolicitud)
    detalle = DetalleSolicitud.objects.get(solicitud=solicitud)
    requerimiento = Requerimiento.objects.get(detalleSolicitud=detalle)
    introduccionln1 = 'En el ejercicio del derecho que me es reconocido en el artículo dos de la Ley de Acceso a la'
    introduccionln2 = 'Información Pública y que deriva del artículo seis de la Constitución de la República, a bien tengo'
    introduccionln3 = 'requerir lo siguiente:'
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment;filename={}{}.pdf'.format(detalle.nombreSolicitante,datetime.datetime.now())

    buffer = BytesIO()
    c = canvas.Canvas(buffer,pagesize=A4)
    nCaracteres = len(requerimiento.peticion)
    print (nCaracteres)
    w,h = A4
    text = c.beginText(50,670)
    text.setFont("Helvetica",10)
    lineas = 0
    requerimiento.peticion,lineas = acotarCadenas(requerimiento.peticion)
    text.textLines(requerimiento.peticion)

    c.setLineWidth(.3)
    c.setFont('Helvetica',13)
    c.drawString(480,750,datetime.datetime.now().strftime('%d/%m/%y'))
    c.line(460,747,560,747)
    c.drawString(30,735,'Oficial de Informacion')
    c.setFont('Helvetica',10)
    c.drawString(50,720,introduccionln1)
    c.drawString(50,705,introduccionln2)
    c.drawString(50,690,introduccionln3)

    c.drawText(text)

    if detalle.fotoFirma:
        c.drawImage(detalle.fotoFirma.url,30,165,width=100,height=100)

    if solicitud.solicitante:
        if solicitud.solicitante.firma:
            c.drawImage(solicitud.solicitante.firma.url,30,165,width=200,height=100)
    c.drawString(30,150, detalle.nombreSolicitante)
    print (lineas)


    c.save()
    c.showPage()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


def solicitudesMasa(request):

    form = MultiRequerimiento(request.POST)
    context = {}
    lista = {'lista':Municipio.objects.all()}
    context.update(lista)
    context.update({'form':form})

    if request.method == 'POST':
        if form.is_valid():
            solicitud = Solicitud()
            solicitud.save()
            detalle = DetalleSolicitud(solicitud=solicitud)
            detalle.save()
            data = form.cleaned_data
            municipios = data['alcaldias']
            for municipio in municipios:
                requerimiento = Requerimiento(detalleSolicitud=detalle,peticion=data['peticion'],alcaldia=Alcaldia.objects.get(municipio=municipio))
                requerimiento.save()
            print(data)
    return render(request,'solicitudesMasa.html',context)
