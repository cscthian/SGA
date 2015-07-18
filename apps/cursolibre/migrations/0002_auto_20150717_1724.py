# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_auto_20150717_1541'),
        ('cursolibre', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matriculacursolibre',
            name='horario',
        ),
        migrations.AddField(
            model_name='matriculacursolibre',
            name='horario',
            field=models.ManyToManyField(to='asistencia.Horario'),
        ),
    ]
