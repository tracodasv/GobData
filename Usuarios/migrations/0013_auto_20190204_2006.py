# Generated by Django 2.1.3 on 2019-02-05 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0012_auto_20190108_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=25, verbose_name='Rol')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Rol', verbose_name='Rol'),
        ),
    ]
