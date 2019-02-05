# Generated by Django 2.1.3 on 2018-11-27 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.IntegerField(null=True, verbose_name='Telefono Movil'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='contacto',
            field=models.IntegerField(null=True, verbose_name='Contactar a'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='datosResidencia',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.DatosResidencia', verbose_name='Datos de Residencia'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='firma',
            field=models.ImageField(null=True, upload_to=None, verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='institucion',
            field=models.ManyToManyField(blank=True, to='Usuarios.Institucion', verbose_name='Institucion'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nacionalidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Pais', verbose_name='Pais'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nit',
            field=models.IntegerField(null=True, verbose_name='NIT'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nivelEducativo',
            field=models.IntegerField(null=True, verbose_name='Nivel Educativo'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ocupacion',
            field=models.CharField(max_length=100, null=True, verbose_name='Ocupacion'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefonoCasa',
            field=models.IntegerField(null=True, verbose_name='Telefono Casa'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipoPersona',
            field=models.IntegerField(null=True, verbose_name='Tipo de Persona'),
        ),
    ]