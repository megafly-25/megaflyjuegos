# Generated by Django 2.2.6 on 2020-03-18 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0005_auto_20200317_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisitos_completos',
            name='CPU_recomendado',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='requisitos_completos',
            name='Memoria_disk_recomendado',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisitos_completos',
            name='RAM_recomendado',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='requisitos_completos',
            name='SO_recomendado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='requisitos_completos',
            name='Targeta_Grafica_recomendado',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]