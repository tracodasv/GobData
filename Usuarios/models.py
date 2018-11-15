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
            """Unicode representation of Pais."""
            pass
    

class Institucion(models.Model):
        """Model definition for Institucion."""
    
        nombreInstitucion = models.CharField(("Institucion"), max_length=200)

        class Meta:
            """Meta definition for Institucion."""
    
            verbose_name = 'Institucion'
            verbose_name_plural = 'Instituciones'
    
        def __str__(self):
            """Unicode representation of Institucion."""
            pass

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
        """Unicode representation of DatosResidencia."""
        pass


class Persona(models.Model):
    """Model definition for Persona."""

    primerNombre = models.CharField(("Primer Nombre"), max_length=50)
    segundoNombre = models.CharField(("Segundo Nombre"), max_length=50)
    primerApellido = models.CharField(("Primer Apellido"), max_length=50)
    segundoApellido = models.CharField(("Segundo Apellido"), max_length=50)
    dui = models.IntegerField(("DUI"))
    nit = models.IntegerField(("NIT"))
    fechaNacimiento = models.DateField(("Nacimiento"), auto_now=False, auto_now_add=False)
    fechaRegistro = models.DateField(("Registro"), auto_now=False, auto_now_add=True)
    tipoPersona = models.IntegerField(("Tipo de Persona"))
    genero = models.IntegerField(("Genero"))
    telefonoCasa = models.IntegerField(("Telefono Casa"))
    celular = models.IntegerField(("Telefono Movil"))
    nivelEducativo = models.IntegerField(("Nivel Educativo"))
    ocupacion = models.CharField(("Ocupacion"), max_length=100)
    contacto = models.IntegerField(("Contactar a"))
    firma = models.ImageField(("Firma"), upload_to=None, height_field=None, width_field=None, max_length=None)
    nacionalidad = models.ForeignKey(Pais, verbose_name=("Pais"), on_delete=models.CASCADE)
    datosResidencia = models.OneToOneField(DatosResidencia, verbose_name=("Datos de Residencia"), on_delete=models.CASCADE)
    institucion = models.ManyToManyField("Institucion", verbose_name=("Institucion"))

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of Persona."""
        pass
        