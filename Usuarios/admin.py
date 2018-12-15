from django.contrib import admin
from .models import Persona,Pais, DatosResidencia, Institucion

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('dui',
                    'primerNombre',
                    'segundoNombre',
                    'primerApellido',
                    'segundoApellido',)
    search_fields = ('dui',
                    'primerNombre',
                    'segundoNombre',
                    'primerApellido',
                    'segundoApellido',)
    ordering = ('primerApellido',)


class DatosResidenciaAdmin(admin.ModelAdmin):
    list_display = (
        'municipio',
        'linea1',
        'linea2',
    )    
    ordering = ('municipio',)




admin.site.register(Persona,PersonaAdmin)
admin.site.register(Pais)
admin.site.register(DatosResidencia,DatosResidenciaAdmin)
admin.site.register(Institucion)

