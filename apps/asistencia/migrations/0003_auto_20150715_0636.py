# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_auto_20150714_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargaacademica',
            name='horario',
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='horario',
            field=models.ManyToManyField(to='asistencia.Horario'),
        ),
    ]
