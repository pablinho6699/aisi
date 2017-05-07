# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0007_auto_20170217_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='cuerpo',
            field=models.CharField(default='Cuerpo noticia', max_length=1000),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='foto',
            field=models.CharField(default='/static/pagina/noticias/no_foto.png', max_length=50),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='titular',
            field=models.CharField(default='Titular', max_length=50),
        ),
    ]
