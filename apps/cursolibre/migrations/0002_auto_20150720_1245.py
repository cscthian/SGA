# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cursolibre', '0001_initial'),
        ('asistencia', '0002_auto_20150720_1245'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='matriculacursolibre',
            name='alumno',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='matriculacursolibre',
            name='asignatura',
            field=models.ForeignKey(to='cursolibre.AsignaturaLibre'),
        ),
        migrations.AddField(
            model_name='matriculacursolibre',
            name='ciclo',
            field=models.ForeignKey(to='cursolibre.Ciclo'),
        ),
        migrations.AddField(
            model_name='ciclo',
            name='asignatura',
            field=models.ManyToManyField(to='cursolibre.AsignaturaLibre'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='matricula',
            field=models.ForeignKey(to='cursolibre.MatriculaCursoLibre'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='asignatura',
            field=models.ForeignKey(to='cursolibre.AsignaturaLibre'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='aula',
            field=models.ForeignKey(to='asistencia.Aula'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='docente',
            field=models.ForeignKey(to='asistencia.Docente'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='horario',
            field=models.ManyToManyField(to='asistencia.Horario'),
        ),
    ]
