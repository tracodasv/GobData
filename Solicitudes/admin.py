from django.contrib import admin
from .models import Solicitud, DetalleSolicitud, Requerimiento, Etapa


admin.site.register(Solicitud)
admin.site.register(DetalleSolicitud)
admin.site.register(Requerimiento)
admin.site.register(Etapa)
