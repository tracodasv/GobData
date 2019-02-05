# Generated by Django 2.1.3 on 2018-11-29 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitudes', '0008_auto_20181129_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='etapa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Solicitudes.Etapa', verbose_name='Etapa'),
        ),
        migrations.AlterField(
            model_name='detallesolicitud',
            name='duiSolicitante',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='DUI'),
        ),
        migrations.AlterField(
            model_name='detallesolicitud',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='detallesolicitud',
            name='fechaNacimientoSolicitante',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Nacimiento Solicitante'),
        ),
        migrations.AlterField(
            model_name='detallesolicitud',
            name='fotoDocumento',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to=None, verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='detallesolicitud',
            name='fotoFirma',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to=None, verbose_name='firma'),
        ),
        migrations.AlterField(
            model_name='detallesolicitud',
            name='genero',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='alcaldia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alcaldias.Alcaldia', verbose_name='Alcaldia'),
        ),
        migrations.AlterField(
            model_name='requerimiento',
            name='peticion',
            field=models.TextField(blank=True, null=True, verbose_name='Peticion'),
        ),
    ]