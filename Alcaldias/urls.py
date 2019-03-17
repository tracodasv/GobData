from django.urls import path
from django.conf.urls import url,include
from .views import index,MunicipalidadesListView

app_name = 'alcaldias'
urlpatterns = [
    url(r"^$",index ),
	path("solicitudes/<int:pk>",MunicipalidadesListView.as_view(),name='solicitudes'),

]