# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_jugadores_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadores',
            name='foto',
            field=models.CharField(default='/home/pablito/corcubion/corcu/pagina/static/pagina/no_foto.png', max_length=50),
        ),
    ]
