from django import forms 
from .models import Solicitud,DetalleSolicitud,Requerimiento

class SolicitudForm(forms.ModelForm):
    """Form definition for Solicitud."""

    class Meta:
        """Meta definition for Solicitudform."""

        model = Solicitud
        fields = ('',)
