# Generated by Django 2.2.6 on 2020-03-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0004_auto_20200317_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mega_juego',
            name='requisitos',
            field=models.CharField(blank=True, choices=[('Requisitos Bajos', 'Requisitos Bajos'), ('Requisitos Medios', 'Requisitos Medios'), ('Requisitos Altos', 'Requisitos Altos')], default=('Requisitos Bajos', 'Requisitos Bajos'), max_length=50, null=True, verbose_name='Requisitos'),
        ),
    ]