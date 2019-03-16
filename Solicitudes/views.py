import os
from datetime import datetime, date, time, timedelta
import calendar
from django.shortcuts import render,redirect
from django.urls import reverse_lazy    
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
from django.core.mail import EmailMessage
from django.views.generic import ListView
from django.http import HttpResponseRedirect

def home_view(request):
    return render(request,'home.html')

#Regresa una tupla con el texto nuevo y el numero de lineas
def acotarCadenas(texto="""""",caracteresPorLinea=100,variacion=5):
    limMax=caracteresPorLinea
    posicionSalto = 0
    inicioLinea = 0
    limMin = caracteresPorLinea-variacion
    bandera = 0
    nuevo_texto=""""""
    lineas=1
    if len(texto)>caracteresPorLinea:
        while bandera == 0:
            saltoLinea = texto[limMin:limMax]
            linea = texto[inicioLinea:limMax]
            if "\n" in linea:
                posicionSalto = linea.index("\n")+inicioLinea
                inicioLinea = posicionSalto + 1
                limMax = inicioLinea + caracteresPorLinea
                limMin = inicioLinea + caracteresPorLinea - variacion
                nuevo_texto=texto
                lineas += 1

            elif " " in saltoLinea :
                posicionSalto = saltoLinea.index(" ") + limMin
                texto = texto[:posicionSalto]+"\n"+texto[posicionSalto:]
                inicioLinea = posicionSalto+1
                limMax = inicioLinea + caracteresPorLinea
                limMin = inicioLinea + caracteresPorLinea - variacion
                nuevo_texto=texto
                lineas += 1

            elif " " not in saltoLinea:
                while saltoLinea.find(" ") == -1:
                     limMin = limMin-variacion
                     saltoLinea = texto[limMin:limMax]
                posicionSalto = saltoLinea.index(" ") + limMin
                texto = texto[:posicionSalto]+"\n"+texto[posicionSalto:]
                inicioLinea = posicionSalto+1
                limMax = inicioLinea + caracteresPorLinea
                limMin = inicioLinea + caracteresPorLinea - variacion
                nuevo_texto=texto
                lineas += 1

            if limMax >= len(texto): 
                bandera = 1
                return(nuevo_texto,lineas)    
        return(nuevo_texto,lineas)    
    return(texto,lineas)

def generadorDePDF(idSolicitud,idRequerimiento):
    solicitud = Solicitud.objects.get(pk=idSolicitud)
    detalle = DetalleSolicitud.objects.get(solicitud=solicitud)
    requerimiento = Requerimiento.objects.get(detalleSolicitud=detalle,pk=idRequerimiento)
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
    requerimiento.save()
    text.textLines(requerimiento.peticion+"\n\n"+ '''Respecto de la modalidad de entrega, solicito todo en formato digital y/o electrónico.
    Señalo como medio para recibir notificaciones, así como lo solicitado, el correo electrónico <Aqui Correo>''')

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
    c.showPage()

    c.save()
    pdf = buffer.getvalue()
    buffer.close()

    

    response.write(pdf)

    return pdf

def solicitante(request):
    if request.method == 'POST':
        nombreCompleto = request.POST['solicitante']
        documento = request.POST['documento']
        genero = request.POST['genero']
        fechaNacimiento = request.POST['fechaNacimiento']
        email = request.POST['email']
        return redirect()

    return(request)

#Creacion de solicitudes simples
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
        if solicitante:
            solicitud = Solicitud(solicitante = solicitante)
        else:
            solicitud = Solicitud()

        solicitud.save()
        solicitud.fechaRespuesta = solicitud.fechaCreacion + timedelta(days=10)
        solicitud.save()
        noAuth = request.POST['solicitante']
        correo = request.POST['email']
        detalle = DetalleSolicitud(solicitud=solicitud,nombreSolicitante=noAuth,email=correo)
        detalle.save()
        print(request.POST)
        requerimiento = Requerimiento(peticion=requisito,alcaldia=Alcaldia.objects.get(municipio=Municipio.objects.get(nombreMunicipio=alcaldia)),resume=requisito[:50])
        requerimiento.detalleSolicitud = detalle
        requerimiento.save()
        print(requerimiento.peticion)
        if solicitante:
            if solicitante.firma:
                return HttpResponseRedirect(reverse_lazy('solicitudes:doc',args=[solicitud.pk]))
            else:
                return redirect('solicitudes:docs',solicitud=solicitud.pk,detalle=detalle.pk)
        else:
            return redirect('solicitudes:docs',solicitud=solicitud.pk,detalle=detalle.pk)


    return render(request,'Solicitudes/index.html',context)

#Recoleccion de documentos
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

#generador de documentos
def docGen(request,idSolicitud):
    solicitud = Solicitud.objects.get(pk=idSolicitud)
    detalle = DetalleSolicitud.objects.get(solicitud=solicitud)
    requerimiento = Requerimiento.objects.filter(detalleSolicitud=detalle)

    introduccionln1 = 'En el ejercicio del derecho que me es reconocido en el artículo dos de la Ley de Acceso a la'
    introduccionln2 = 'Información Pública y que deriva del artículo seis de la Constitución de la República, a bien tengo'
    introduccionln3 = 'requerir lo siguiente:'
    response = HttpResponse(content_type='application/pdf')
    requerimiento = requerimiento[0]
    #response['Content-Disposition'] = 'attachment;filename={}{}.pdf'.format(detalle.nombreSolicitante,datetime.datetime.now())

    buffer = BytesIO()
    c = canvas.Canvas(buffer,pagesize=A4)
    nCaracteres = len(requerimiento.peticion )
    print (nCaracteres)
    w,h = A4
    text = c.beginText(50,670)
    text.setFont("Helvetica",10)
    lineas = 0
    requerimiento.peticion,lineas = acotarCadenas(requerimiento.peticion)
    requerimiento.save()
    text.textLines(requerimiento.peticion+"\n\n"+ '''Respecto de la modalidad de entrega, solicito todo en formato digital y/o electrónico.
    Señalo como medio para recibir notificaciones, así como lo solicitado, el correo electrónico <Aqui Correo>''')

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
    c.showPage()

    c.save()
    pdf = buffer.getvalue()
    buffer.close()

    email = EmailMessage(subject='Hello', body='Body',to=[requerimiento.alcaldia.oficial] )
    email.attach('Solicitud.pdf', pdf , 'application/pdf')
    #email.send()
    print(email)

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
            solicitante = Persona.objects.get(usuario=request.user)
            nombre = solicitante.primerNombre + " " + solicitante.segundoNombre + solicitante.primerApellido + " " + solicitante.segundoApellido
            solicitud = Solicitud(solicitante=solicitante)
            solicitud.save()
            solicitud.fechaRespuesta = solicitud.fechaCreacion + timedelta(days=10)
            solicitud.save()
            detalle = DetalleSolicitud(solicitud=solicitud,nombreSolicitante=nombre)
            detalle.save()

            data = form.cleaned_data
            municipios = data['alcaldias']
            municipios=municipios.split(",")
            correos = []
            requerimiento = ''

            for municipio in municipios:
                municipalidad = Municipio.objects.get(nombreMunicipio=municipio)
                alcaldia = Alcaldia.objects.get(municipio=municipalidad)
                requerimiento = Requerimiento(detalleSolicitud=detalle,
                    peticion=data['peticion'],
                    alcaldia=alcaldia,
                    resume=data['peticion'][:50])
                requerimiento.save()
                correos.append(alcaldia.oficial)

                

            pk=solicitud.pk

            pdf = generadorDePDF(pk,requerimiento.pk)

            email = EmailMessage(subject='Solicitud de Informacion', 
                                body='''Oficial de informacion: en uso de las facultades legales, le pido que atienda la solicitud. Correo generado con GOBDATA. 
                                        Adjunto PDF de peticion de informacion''',
                                bcc=correos)
            email.attach('Solicitud.pdf', pdf , 'application/pdf')

            email.send()

            print(email.recipients())
            print("Se ha enviado correo")

    return render(request,'solicitudesMasa.html',context)


class RequerimientoListView(ListView):
    template_name = "Solicitudes/solicitudlist.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Requerimiento.objects.filter(
            detalleSolicitud__solicitud__solicitante=Persona.objects.get(
                usuario=self.request.user))
        return queryset
    

