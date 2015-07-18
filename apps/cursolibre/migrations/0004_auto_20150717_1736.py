# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_auto_20150717_1541'),
        ('cursolibre', '0003_auto_20150717_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asignatura', models.ForeignKey(to='cursolibre.AsignaturaLibre')),
                ('aula', models.ForeignKey(to='asistencia.Aula')),
                ('docente', models.ForeignKey(to='asistencia.Docente')),
                ('horario', models.ManyToManyField(to='asistencia.Horario')),
            ],
        ),
        migrations.RemoveField(
            model_name='matriculacursolibre',
            name='aula',
        ),
        migrations.RemoveField(
            model_name='matriculacursolibre',
            name='docente',
        ),
        migrations.RemoveField(
            model_name='matriculacursolibre',
            name='horario',
        ),
    ]
