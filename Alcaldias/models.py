from django.db import models


class Departamento(models.Model):
    """Model definition for Departamento."""

    nombreDepartamento = models.CharField(("Nombre"), max_length=50)
    class Meta:
        """Meta definition for Departamento."""
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        """Unicode representation of Departamento."""
        return self.nombreDepartamento


class Municipio(models.Model):
    """Model definition for Municipio."""
    nombreMunicipio = models.CharField(("Municipio"), max_length=50)
    departamento = models.ForeignKey("Departamento", verbose_name=("Departamento"), on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Municipio."""

        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return '{}'.format(self.nombreMunicipio)


class Alcaldia(models.Model):
    """Model definition for Alcaldia."""

    municipio = models.OneToOneField(Municipio, verbose_name=("Municipio"), on_delete=models.CASCADE)
    oficial = models.EmailField(verbose_name="Correo",blank=True,null=True)

    class Meta:
        """Meta definition for Alcaldia."""
        verbose_name = 'Alcaldia'
        verbose_name_plural = 'Alcaldias'

    def __str__(self):
        return '{} - {}'.format(self.municipio, self.municipio.departamento)
