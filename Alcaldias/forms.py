from django import forms

from .Alcaldias import Alcaldia,Municipio,Departamento



class DepartamentoForm(forms.ModelForm):
    
    class Meta:
        model = "Departamento",
        fields = ()

