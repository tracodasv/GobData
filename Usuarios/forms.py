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
                    ]
        labels = {
                    'primerNombre':'Primer Nombre',
                    'segundoNombre':'Segundo Nombre',
                    'primerApellido':'Primer Apellido',
                    'segundoApellido':'Segundo Apellido',
                    'dui':'DUI',
                    'fechaNacimiento':'Fecha De Nacimiento',
                    }

        widgets = {
                    'primerNombre':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'}),
                    'segundoNombre':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'}),
                    'primerApellido':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'}),
                    'segundoApellido':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'}),
                    'dui':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'}),
                    'fechaNacimiento':forms.TextInput(attrs={'class':'form-control col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12','type':'date'}),
        }