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
                ('slug', models.SlugField(null=True, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_carrera', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('siglas', models.CharField(max_length=4, verbose_name=b'Abrebiatura')),
                ('titulo', models.CharField(max_length=50, verbose_name=b'Licenciatura')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=7, choices=[(b'Ma\xc3\xb1ana1', b'7:00 am - 11:30 am'), (b'Ma\xc3\xb1ana2', b'8:30 am - 1:00 pm'), (b'Tarde', b'1:00 pm - 5:30 pm'), (b'Noche', b'5:30 pm - 10:00 pm')])),
                ('fecha_matricula', models.DateTimeField()),
                ('periodo', models.CharField(max_length=50, verbose_name=b'tiempo duracion')),
                ('estado_matricula', models.BooleanField()),
                ('alumno', models.ForeignKey(to='matricula.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vacantes', models.PositiveIntegerField()),
                ('inicio_labores', models.DateField()),
                ('fin_labores', models.DateField()),
                ('semestre', models.CharField(max_length=20)),
                ('finalizado', models.BooleanField(default=False)),
            ],
        ),
    ]
