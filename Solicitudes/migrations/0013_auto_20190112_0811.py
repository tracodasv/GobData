# Generated by Django 2.1.3 on 2019-01-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitudes', '0012_auto_20181227_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallesolicitud',
            name='fotoDocumento',
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='documentoAnterior',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='documentos/', verbose_name='Documento(vista Anterior)'),
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='documentoPosterior',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='documentos/', verbose_name='Documento(vista Posterior)'),
        ),
        migrations.AlterField(
            model_name='detallesolicitud',
            name='fotoFirma',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='firmas/', verbose_name='firma'),
        ),
    ]
