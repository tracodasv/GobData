from django.db import models
from django.urls import reverse
from Alcaldias.models import Municipio,Alcaldia
from Usuarios.models import Persona


class Requerimiento(models.Model):
    categoria = models.CharField(("Categoria"),blank=True, max_length=50)
    detalle = models.TextField(("Lo que solicita"))

    class Meta:
        verbose_name = ("Requerimiento")
        verbose_name_plural = ("Requerimientos")

    def get_absolute_url(self):
        return reverse("Requerimiento_detail", kwargs={"pk": self.pk})



class DetalleSolicitud(models.Model):
    
    firmaSolicitante = models.ImageField(("Firma"), upload_to=None, height_field=None, width_field=None, max_length=None)
    persona = models.ForeignKey(Persona, verbose_name=("Solicitante"), on_delete=models.CASCADE,blank=True,null=True)
    requerimiento = models.ForeignKey("Requerimiento", verbose_name=("Requerimiento"), on_delete=models.CASCADE)
    alcaldia = models.ForeignKey(Alcaldia, verbose_name=("Alcaldia"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("DetalleSolicitud")
        verbose_name_plural = ("DetalleSolicitudes")

    def __str__(self):
        return self.persona.PrimerNombre

    def get_absolute_url(self):
        return reverse("DetalleSolicitud_detail", kwargs={"pk": self.pk})


class Etapa(models.Model):
    progreso = models.IntegerField(("Progreso de Solicitud"))
    nombreEtapa = models.CharField(("Etapa"), max_length=50)
    

    class Meta:
        verbose_name = ("Etapa")
        verbose_name_plural = ("Etapas")

    def __str__(self):
        return (self.nombreEtapa)

    def get_absolute_url(self):
        return reverse("Etapa_detail", kwargs={"pk": self.pk})


class Solicitud(models.Model):

    fechaCreacion = models.DateField(("Apertura De Solicitud"),auto_now=False, auto_now_add=True)
    fechaModificacion = models.DateField(("Ultima Modificacion"),auto_now=True, auto_now_add=False)
    estado = models.CharField(("Estado"), max_length=100)
    etapa = models.ForeignKey("Etapa", on_delete=models.CASCADE)
    detalleSolicitud = models.OneToOneField(DetalleSolicitud, verbose_name=("Detalle Solicitud"), on_delete=models.CASCADE) 

    class Meta:
        verbose_name = ("Solicitud")
        verbose_name_plural = ("Solicitudes")

    def __str__(self):
        return (self.fechaCreacion)

    def get_absolute_url(self):
        return reverse("Solicitud_detail", kwargs={"pk": self.pk})
