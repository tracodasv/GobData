# Generated by Django 2.1.3 on 2018-11-29 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitudes', '0005_auto_20181115_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='estado',
        ),
    ]
