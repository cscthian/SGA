# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0004_auto_20150627_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistenciadocente',
            name='carga_academica',
        ),
        migrations.RemoveField(
            model_name='cargaacademica',
            name='asignatura',
        ),
        migrations.RemoveField(
            model_name='cargaacademica',
            name='aula',
        ),
        migrations.RemoveField(
            model_name='cargaacademica',
            name='docente',
        ),
        migrations.RemoveField(
            model_name='cargaacademica',
            name='horario',
        ),
        migrations.DeleteModel(
            name='AsistenciaDocente',
        ),
        migrations.DeleteModel(
            name='Aula',
        ),
        migrations.DeleteModel(
            name='CargaAcademica',
        ),
        migrations.DeleteModel(
            name='Horario',
        ),
    ]
