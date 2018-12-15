from django.urls import path
from django.conf.urls import url,include,nuevasolicitud
from .views import index

app_name = 'solicitudes'
urlpatterns = [
    url(r"^$", index, name="index"),
    path('nuevaSolicitud/', nuevasolicitud, name='nuevaSolicitud'),
]
 