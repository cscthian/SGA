# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_modulo', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('carrera_profesional', models.ForeignKey(to='matricula.Carrera')),
            ],
        ),
    ]
