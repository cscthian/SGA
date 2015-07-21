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
                ('codigo', models.CharField(unique=True, max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=15, choices=[(b'obligatorio', b'obligatorio'), (b'opcional', b'opcional')])),
                ('horas_teorica', models.PositiveIntegerField(default=0)),
                ('horas_practica', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=2, verbose_name=b'Nombre', choices=[(b'1', b'Modulo 1'), (b'2', b'Modulo 2'), (b'3', b'Modulo 3'), (b'4', b'Modulo 4'), (b'5', b'Modulo 5'), (b'6', b'Modulo 6')])),
                ('costo', models.DecimalField(max_digits=7, decimal_places=2)),
                ('asignatura', models.ManyToManyField(to='notas.Asignatura')),
                ('carrera', models.ForeignKey(to='matricula.Carrera')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Modulos',
            },
        ),
        migrations.CreateModel(
            name='Nota',
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
            ],
        ),
    ]
