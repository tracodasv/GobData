from django.db import models



class Solicitud(models.Model):

    

    class Meta:
        verbose_name = _("Solicitud")
        verbose_name_plural = _("Solicitudes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Solicitud_detail", kwargs={"pk": self.pk})

