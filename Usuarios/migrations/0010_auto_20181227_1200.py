# Generated by Django 2.1.3 on 2018-12-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0009_auto_20181227_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fechaNacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Nacimiento'),
        ),
    ]
