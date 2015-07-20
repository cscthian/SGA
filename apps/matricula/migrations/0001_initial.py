# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'nombre')),
                ('siglas', models.CharField(max_length=4, verbose_name=b'abrebiatura')),
                ('titulo', models.CharField(max_length=50, verbose_name=b'licenciatura')),
            ],
            options={
                'verbose_name_plural': 'Carreras',
            },
        ),
        migrations.CreateModel(
            name='CursosCargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_matricula', models.DateTimeField()),
                ('estado_matricula', models.BooleanField(default=False)),
                ('saldo', models.DecimalField(default=600, max_digits=12, decimal_places=2)),
                ('completado', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(to='matricula.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vacantes', models.PositiveIntegerField()),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('semestre', models.CharField(unique=True, max_length=20)),
                ('finalizado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['inicio'],
                'verbose_name_plural': 'Programaciones',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.CharField(max_length=1)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
    ]
