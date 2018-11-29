from django.urls import path
from django.conf.urls import url,include
from .views import index
app_name = 'solicitudes'
urlpatterns = [
    url(r"^$",index,name='index' )
    #url(r"^usuarios/$", include('usuarios.urls',namespace='usuarios')),
    
]
