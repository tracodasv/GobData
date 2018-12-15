# Generated by Django 2.1.3 on 2018-11-29 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0004_auto_20181129_0048'),
        ('Solicitudes', '0007_auto_20181129_0551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallesolicitud',
            options={'verbose_name': 'DetalleSolicitud', 'verbose_name_plural': 'DetalleSolicituds'},
        ),
        migrations.RemoveField(
            model_name='detallesolicitud',
            name='firmaSolicitante',
        ),
        migrations.RemoveField(
            model_name='detallesolicitud',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='detallesolicitud',
            name='requerimiento',
        ),
        migrations.RemoveField(
            model_name='etapa',
            name='progreso',
        ),
        migrations.RemoveField(
            model_name='requerimiento',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='requerimiento',
            name='detalle',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='detalleSolicitud',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='etapa',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='fechaModificacion',
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='duiSolicitante',
            field=models.CharField(default=None, max_length=10, verbose_name='DUI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='email',
            field=models.EmailField(default=None, max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='fechaNacimientoSolicitante',
            field=models.DateTimeField(default=None, verbose_name='Nacimiento Solicitante'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='fotoDocumento',
            field=models.FileField(default=None, max_length=250, upload_to=None, verbose_name='Documento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='fotoFirma',
            field=models.FileField(default=None, max_length=250, upload_to=None, verbose_name='firma'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='genero',
            field=models.CharField(default=None, max_length=1, verbose_name='Genero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='nombreSolicitante',
            field=models.CharField(default=None, max_length=200, verbose_name='Solicitante'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='solicitud',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Solicitudes.Solicitud', verbose_name='Solicitud'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requerimiento',
            name='detalleSolicitud',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Solicitudes.DetalleSolicitud', verbose_name='Detalle de Solicitud'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requerimiento',
            name='peticion',
            field=models.TextField(default=None, verbose_name='Peticion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='Solicitante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Persona', verbose_name='Solicitante'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='nombreEtapa',
            field=models.CharField(max_length=100, verbose_name='Etapa'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fechaCreacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion'),
        ),
    ]
