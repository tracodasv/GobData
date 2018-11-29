from django.db import models
from Alcaldias.models import Municipio

class Pais(models.Model):
        """Model definition for Pais."""
    
        nombrePais = models.CharField(("Pais"), max_length=100)
        codigoPais = models.CharField(("Codigo Pais"), max_length=10,unique=True)


        class Meta:
            """Meta definition for Pais."""
    
            verbose_name = 'Pais'
            verbose_name_plural = 'Paises'
        
        def __str__(self):
            return self.nombrePais

    
       
    

class Institucion(models.Model):
        """Model definition for Institucion."""
    
        nombreInstitucion = models.CharField(("Institucion"), max_length=200)

        class Meta:
            """Meta definition for Institucion."""
    
            verbose_name = 'Institucion'
            verbose_name_plural = 'Instituciones'

        def __str__(self):
            return self.nombreInstitucion
    
       

class DatosResidencia(models.Model):
    """Model definition for DatosResidencia."""
    linea1 = models.CharField(("Direccion 1"), max_length=100)
    linea2 = models.CharField(("Direccion 2"), max_length=100)
    municipio = models.ForeignKey(Municipio, verbose_name=("Municipio"), on_delete=models.CASCADE)


    class Meta:
        """Meta definition for DatosResidencia."""

        verbose_name = 'DatosResidencia'
        verbose_name_plural = 'DatosResidencias'
   
    def __str__(self):
        return self.linea1



class Persona(models.Model):
    """Model definition for Persona."""

    primerNombre = models.CharField(("Primer Nombre"), max_length=50)
    segundoNombre = models.CharField(("Segundo Nombre"), max_length=50)
    primerApellido = models.CharField(("Primer Apellido"), max_length=50)
    segundoApellido = models.CharField(("Segundo Apellido"), max_length=50)
    dui = models.CharField(("DUI"), max_length=10,blank=True,null=True)
    nit = models.CharField(("NIT"), max_length=17,blank=True,null=True)
    fechaNacimiento = models.DateField(("Nacimiento"), auto_now=False, auto_now_add=False)
    fechaRegistro = models.DateField(("Registro"), auto_now=False, auto_now_add=True)
    tipoPersona = models.IntegerField(("Tipo de Persona"),null=True,blank=True)
    genero = models.IntegerField(("Genero"),blank=True,null=True)
    telefonoCasa = models.IntegerField(("Telefono Casa"),null=True,blank=True)
    celular = models.IntegerField(("Telefono Movil"),null=True,blank=True)
    nivelEducativo = models.IntegerField(("Nivel Educativo"),null=True,blank=True)
    ocupacion = models.CharField(("Ocupacion"), max_length=100,null=True,blank=True)
    contacto = models.IntegerField(("Contactar a"),null=True,blank=True)
    firma = models.ImageField(("Firma"), upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)
    nacionalidad = models.ForeignKey(Pais, verbose_name=("Pais"), on_delete=models.CASCADE,null=True,blank=True)
    datosResidencia = models.OneToOneField(DatosResidencia, verbose_name=("Datos de Residencia"), on_delete=models.CASCADE,null=True,blank=True)
    institucion = models.ManyToManyField("Institucion", verbose_name=("Institucion"),blank=True)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.primerApellido