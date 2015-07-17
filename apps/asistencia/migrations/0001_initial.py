# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsistenciaAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Asistencia del alumno',
            },
        ),
        migrations.CreateModel(
            name='AsistenciaDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_Inicio', models.DateTimeField(null=True, blank=True)),
                ('hora_Fin', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Asistencia del docente',
            },
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_aula', models.CharField(max_length=50, verbose_name=b'numero de Aula')),
                ('piso', models.CharField(max_length=50)),
                ('tipo_aula', models.CharField(max_length=1, choices=[(b'L', b'laboratorio'), (b'T', b'teoria')])),
                ('capacidad', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Aulas',
            },
        ),
        migrations.CreateModel(
            name='CargaAcademica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Carga academica',
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_docente', models.CharField(max_length=12, choices=[(b'contratado', b'contratado'), (b'nombrado', b'nombrado')])),
                ('especialidad', models.CharField(max_length=2, choices=[(b'1', b'administracion de bases de datos'), (b'2', b'analista de sistemas'), (b'3', b'administracion de centros de computo'), (b'4', b'cursos generales')])),
                ('titulo', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.CharField(max_length=10, choices=[(b'lunes', b'lunes'), (b'martes', b'martes'), (b'miercoles', b'miercoles'), (b'jueves', b'jueves'), (b'viernes', b'viernes'), (b'sabado', b'sabado')])),
                ('hora_inicio', models.TimeField(null=True, blank=True)),
                ('hora_final', models.TimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ['dia', 'hora_inicio'],
                'verbose_name_plural': 'Horarios',
            },
        ),
        migrations.AlterUniqueTogether(
            name='horario',
            unique_together=set([('dia', 'hora_inicio', 'hora_final')]),
        ),
    ]
