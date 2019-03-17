from django.shortcuts import render
from django.http import HttpResponse
from .models import Alcaldia,Municipio
from Solicitudes.models import Solicitud,DetalleSolicitud,Requerimiento
from django.views.generic import ListView



def index(request):
    return render(request,"Alcaldias/municipalidades.html")
	
	
class MunicipalidadesListView(ListView):
    template_name = "Alcaldias/municipalidades.html"
    paginate_by = 10
	
    def get_queryset(self):
        queryset = Requerimiento.objects.filter(alcaldia__pk=self.kwargs['pk'])
        return queryset
