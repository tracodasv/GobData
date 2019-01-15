from django.urls import path
from django.conf.urls import url,include
from .views import nuevaSolicitud,recoleccion_de_documentos,docGen

app_name = 'solicitudes'
urlpatterns = [
    #url(r"^$", index, name="index"),
    path('nuevaSolicitud/', nuevaSolicitud, name='nuevaSolicitud'),
    path('completarInformacionDocs/<int:solicitud>/<int:detalle>',recoleccion_de_documentos,name='docs'),
    path('docSolicitud/<int:idSolicitud>', docGen, name="doc")
]
 