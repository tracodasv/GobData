# Generated by Django 2.1.3 on 2018-12-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitudes', '0010_auto_20181130_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallesolicitud',
            name='fechaNacimientoSolicitante',
            field=models.DateField(blank=True, null=True, verbose_name='Nacimiento Solicitante'),
        ),
    ]
