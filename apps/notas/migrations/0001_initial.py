# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
        ('matricula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=4)),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=15, choices=[(b'obligatorio', b'obligatorio'), (b'opcional', b'opcional')])),
                ('creditos', models.PositiveIntegerField(default=0)),
                ('horas_teoricas', models.PositiveIntegerField(default=0)),
                ('horas_practicas', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'nombre')),
                ('carrera', models.ForeignKey(to='matricula.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota1', models.CharField(default=b'--', max_length=20, verbose_name=b'PP1')),
                ('nota2', models.CharField(default=b'--', max_length=20, verbose_name=b'PP2')),
                ('nota3', models.CharField(default=b'--', max_length=20, verbose_name=b'PP3')),
                ('nota4', models.CharField(default=b'--', max_length=20, verbose_name=b'PP4')),
                ('promedio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('asignatura', models.ForeignKey(to='notas.Asignatura')),
                ('docente', models.ForeignKey(to='asistencia.Docente')),
                ('matricula', models.ForeignKey(to='matricula.Matricula')),
                ('programacion', models.ForeignKey(to='matricula.Programacion')),
            ],
        ),
        migrations.AddField(
            model_name='asignatura',
            name='modulo',
            field=models.ForeignKey(to='notas.Modulo'),
        ),
    ]
