# Generated by Django 2.1.3 on 2018-11-29 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_auto_20181127_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefono Movil'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='contacto',
            field=models.IntegerField(blank=True, null=True, verbose_name='Contactar a'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='datosResidencia',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.DatosResidencia', verbose_name='Datos de Residencia'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='firma',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='genero',
            field=models.IntegerField(blank=True, null=True, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nacionalidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Pais', verbose_name='Pais'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nivelEducativo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nivel Educativo'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ocupacion'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefonoCasa',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefono Casa'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipoPersona',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tipo de Persona'),
        ),
    ]
