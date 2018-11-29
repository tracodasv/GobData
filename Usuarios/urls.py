from django.urls import path
from django.conf.urls import url,include
from .views import index, PersonaFormulario

app_name='usuarios'
urlpatterns = [
    url(r"^$", index),
    url(r"datosPersonales/$",PersonaFormulario,name='datosP')
    #url(r"^usuarios/$", include('usuarios.urls',namespace='usuarios')),
    
]
