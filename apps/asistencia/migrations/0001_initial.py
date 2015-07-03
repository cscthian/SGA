# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsistenciaDocente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_Inicio', models.DateTimeField(null=True, blank=True)),
                ('hora_Fin', models.DateTimeField(null=True, blank=True)),
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
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_docente', models.CharField(max_length=12, choices=[(b'contratado', b'contratado'), (b'nombrado', b'nombrado')])),
                ('especialidad', models.CharField(max_length=2, choices=[(b'1', b'administracion de bases de datos'), (b'2', b'analista de sistemas'), (b'3', b'administracion de centros de computo'), (b'4', b'cursos generales')])),
                ('titulo', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.DateField(null=True, blank=True)),
                ('hora_inicio', models.TimeField(null=True, blank=True)),
                ('hora_final', models.TimeField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='docente',
            field=models.ForeignKey(to='asistencia.Docente'),
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
