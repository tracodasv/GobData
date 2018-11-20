from django.urls import path
from django.conf.urls import url,include
from .views import index

urlpatterns = [
    url(r"^$",index )
    #url(r"^usuarios/$", include('usuarios.urls',namespace='usuarios')),
    
]