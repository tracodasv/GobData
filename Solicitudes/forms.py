from django import forms 
from .models import Solicitud,DetalleSolicitud,Requerimiento

class DetalleSolicitudForm(forms.ModelForm):
    """Form definition for DetalleSolicitud."""

    class Meta:
        """Meta definition for DetalleSolicitudform."""

        model = DetalleSolicitud
        fields = (
            'nombreSolicitante',
            'documentoSolicitante' ,
            'fechaNacimientoSolicitante',
            'email',
            'genero')

        labels = {
            'nombreSolicitante':'Nombre',
            'documentoSolicitante':'Documento de Identidad' ,
            'fechaNacimientoSolicitante':'Fecha De Nacimiento',
            'email':'E-mail',
            'genero':'Genero'
        }

        widgets={
            'nombreSolicitante':forms.TextInput(attrs={'class':'form-control','type':"text"}),
            'documentoSolicitante':forms.TextInput(attrs={'class':'form-control','type':"number"}),
            'fechaNacimientoSolicitante':forms.TextInput(attrs={'class':'form-control','type':"date"}),
            'email':forms.TextInput(attrs={'class':'form-control','type':"email"}),
            
        }




class RequerimientoForm(forms.ModelForm):
    
    class Meta:
        model = "Requerimiento",
        fields = ("",)
