from django import forms
from .models import Solicitud,DetalleSolicitud,Requerimiento
from Alcaldias.models import Alcaldia,Municipio
from tags_input import fields


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



class MultiRequerimiento(forms.Form):
    alcaldias = fields.TagsInputField(
        Municipio.objects.all(),
        create_missing=False,
        required = True,
        widget = forms.TextInput(attrs={'class':'form-control','value':'','type':'text','data-role':'tagsinput','placeholder':'Ingrese las alcaldias'}) 
    )
    peticion = forms.CharField(
        widget = forms.Textarea(attrs={'class':'form-control','id':'peticion','name':'peticion','rows':'5'})
    )
