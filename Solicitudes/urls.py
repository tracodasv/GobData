from django.urls import path
from django.conf.urls import url,include
from .views import nuevaSolicitud,recoleccion_de_documentos,docGen,generador_pdf_DUI,solicitudesMasa,RequerimientoListView

app_name = 'solicitudes'
urlpatterns = [
    #url(r"^$", index, name="index"),
    path('nuevaSolicitud/', nuevaSolicitud, name='nuevaSolicitud'),
    path('completarInformacionDocs/<int:solicitud>/<int:detalle>',recoleccion_de_documentos,name='docs'),
    path('docSolicitud/<int:idSolicitud>', docGen, name="doc"),
    path("solicitudesMasa/", solicitudesMasa, name="solicitudesMasa"),
    path("misSolicitudes/",RequerimientoListView.as_view(),name='misSolicitudes'),
    path("dui/<int:idSolicitud>", generador_pdf_DUI, name="dui")
]
 