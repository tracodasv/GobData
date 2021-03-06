from django import forms
from .models import Persona,Pais

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
                    'primerNombre',
                    'segundoNombre',
                    'primerApellido',
                    'segundoApellido',
                    'dui',
                    'fechaNacimiento',
                    'nit',
                    ]
        labels = {
                    'primerNombre':'Primer Nombre',
                    'segundoNombre':'Segundo Nombre',
                    'primerApellido':'Primer Apellido',
                    'segundoApellido':'Segundo Apellido',
                    'dui':'DUI',
                    'fechaNacimiento':'Fecha De Nacimiento',
                    'nit':'NIT',
                    }

        widgets = {
                    'primerNombre':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'}),
                    'segundoNombre':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'}),
                    'primerApellido':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'}),
                    'segundoApellido':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'}),
                    'dui':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12','type':'number'}),
                    'nit':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12','type':'number'}),
                    'fechaNacimiento':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12','type':'date'}),
                    }

class DocumentosForm(forms.Form):

    firma = forms.ImageField()
    documentoFotoAnterior = forms.ImageField()
    documentoFotoPosterior = forms.ImageField()
