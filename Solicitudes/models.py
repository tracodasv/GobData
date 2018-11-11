from django.db import models
from django.urls import reverse

class Solicitud(models.Model):

    fechaCreacion = models.DateField(("Apertura De Solicitud"),auto_now=False, auto_now_add=True)
    fechaModificacion = models.DateField(("Ultima Modificacion"),auto_now=True, auto_now_add=False)
    estado = models.CharField(("Estado"), max_length=100)
    etapa = models.ForeignKey("Etapa", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Solicitud")
        verbose_name_plural = ("Solicitudes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Solicitud_detail", kwargs={"pk": self.pk})


class DetalleSolicitud(models.Model):
    
    firmaSolicitante = models.ImageField(("Firma"), upload_to=None, height_field=None, width_field=None, max_length=None)
    solicitante = models.CharField(("Solicitante"), max_length=200)
    solicitud = models.ForeignKey("Solicitud", on_delete=models.CASCADE) 

    class Meta:
        verbose_name = ("DetalleSolicitud")
        verbose_name_plural = ("DetalleSolicitudes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DetalleSolicitud_detail", kwargs={"pk": self.pk})


class Requerimiento(models.Model):
    categoria = models.CharField(("Categoria"),blank=True, max_length=50)
    detalle = models.TextField(("Lo que solicita"))
    detalleSolicitud = models.ForeignKey("DetalleSolicitud", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Requerimiento")
        verbose_name_plural = ("Requerimientos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Requerimiento_detail", kwargs={"pk": self.pk})


class Etapa(models.Model):
    progreso = models.IntegerField(("Progreso de Solicitud"))
    nombreEtapa = models.CharField(("Etapa"), max_length=50)
    

    class Meta:
        verbose_name = ("Etapa")
        verbose_name_plural = ("Etapas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Etapa_detail", kwargs={"pk": self.pk})
