from django.db import models
from django.urls import reverse
from Alcaldias.models import Municipio,Alcaldia
from Usuarios.models import Persona

class Etapa(models.Model):
    """Model definition for Etapa."""

    nombreEtapa = models.CharField(("Etapa"), max_length=100)

    class Meta:
        """Meta definition for Etapa."""

        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'

    def __str__(self):
        """Unicode representation of Etapa."""
        return '{}'.format(self.nombreEtapa)


class Solicitud(models.Model):
    """Model definition for Solicitud."""

    fechaCreacion = models.DateTimeField(("Fecha de Creacion"), auto_now=False, auto_now_add=True)
    solicitante = models.ForeignKey(Persona, verbose_name=("Solicitante"), on_delete=models.CASCADE,blank=True,null=True)
    etapa = models.ForeignKey(Etapa, verbose_name=("Etapa"), on_delete=models.CASCADE ,blank=True,null=True)
    class Meta:
        """Meta definition for Solicitud."""

        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'

    def __str__(self):
        """Unicode representation of Solicitud."""
        if self.solicitante != None:
            return '{} {}'.format(self.solicitante,self.fechaCreacion)  
        else:
            return '{} {}'.format(DetalleSolicitud.objects.filter(solicitud=self)[0].nombreSolicitante,self.fechaCreacion)  

class DetalleSolicitud(models.Model):
    """Model definition for DetalleSolicitud."""

    nombreSolicitante = models.CharField(("Solicitante"), max_length=200,blank=True,null=True)
    documentoSolicitante = models.CharField(("DUI"), max_length=10,blank=True,null=True)
    solicitud = models.OneToOneField(Solicitud, verbose_name=("Solicitud"), on_delete=models.CASCADE)
    fotoFirma = models.FileField(("firma"), upload_to='firmas/', max_length=250,blank=True,null=True)
    documentoAnterior = models.FileField(("Documento(vista Anterior)"), upload_to='documentos/', max_length=250,blank=True,null=True)
    documentoPosterior = models.FileField(("Documento(vista Posterior)"), upload_to='documentos/', max_length=250,blank=True,null=True)
    fechaNacimientoSolicitante = models.DateField(("Nacimiento Solicitante"), auto_now=False, auto_now_add=False,blank=True,null=True)
    email = models.EmailField(("E-mail"), max_length=254,blank=True,null=True)
    genero = models.CharField(("Genero"), max_length=1,blank=True,null=True)


    class Meta:
        """Meta definition for DetalleSolicitud."""

        verbose_name = 'DetalleSolicitud'
        verbose_name_plural = 'DetalleSolicituds'

    def __str__(self):
        """Unicode representation of DetalleSolicitud."""
        return '{}'.format(self.solicitud)

class Requerimiento(models.Model):
    """Model definition for Requerimiento."""
    
    detalleSolicitud = models.ForeignKey(DetalleSolicitud, verbose_name=("Detalle de Solicitud"), on_delete=models.CASCADE)
    peticion = models.TextField(("Peticion"),blank=True,null=True)
    alcaldia = models.ForeignKey(Alcaldia, verbose_name=("Alcaldia"), on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        """Meta definition for Requerimiento."""

        verbose_name = 'Requerimiento'
        verbose_name_plural = 'Requerimientos'

    def __str__(self):
        """Unicode representation of Requerimiento."""
        return '{} {}'.format(self.alcaldia,self.detalleSolicitud)
