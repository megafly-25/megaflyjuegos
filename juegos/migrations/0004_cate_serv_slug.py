# Generated by Django 2.2.6 on 2020-03-15 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0003_auto_20200315_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='cate_serv',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
