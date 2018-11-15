from django.db import models

# Create your models here.

class Alcaldia(models.Model):
    """Model definition for Alcaldia."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Alcaldia."""
        municipio = models.OneToOneField("Municipio", verbose_name=("Municipio"), on_delete=models.CASCADE)
        verbose_name = 'Alcaldia'
        verbose_name_plural = 'Alcaldias'

    def __str__(self):
        """Unicode representation of Alcaldia."""
        pass


class Municipio(models.Model):
    """Model definition for Municipio."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Municipio."""

        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        departamento = models.ForeignKey("Departamento", verbose_name=("Departamento"), on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Municipio."""
        pass


class Departamento(models.Model):
    """Model definition for Departamento."""
    nombreDepartamento = models.CharField(("Nombre"), max_length=50)
    
    class Meta:
        """Meta definition for Departamento."""

        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        """Unicode representation of Departamento."""
        pass

