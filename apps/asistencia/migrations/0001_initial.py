# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0005_auto_20150701_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsistenciaDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_Inicio', models.DateTimeField()),
                ('hora_Fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_aula', models.CharField(max_length=50, verbose_name=b'numero de Aula')),
                ('piso', models.CharField(max_length=50)),
                ('tipo_aula', models.CharField(max_length=1, choices=[(b'L', b'Laboratorio'), (b'T', b'Teoria')])),
                ('capacidad', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CargaAcademica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asignatura', models.ForeignKey(to='academico.Asignatura')),
                ('aula', models.ForeignKey(to='asistencia.Aula')),
                ('docente', models.ForeignKey(to='academico.Docente')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='horario',
            field=models.ForeignKey(to='asistencia.Horario'),
        ),
        migrations.AddField(
            model_name='asistenciadocente',
            name='carga_academica',
            field=models.ForeignKey(to='asistencia.CargaAcademica'),
        ),
    ]
