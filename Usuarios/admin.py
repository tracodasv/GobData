from django.contrib import admin
from .models import Persona,Pais, DatosResidencia, Institucion

admin.site.register(Persona)
admin.site.register(Pais)
admin.site.register(DatosResidencia)
admin.site.register(Institucion)

