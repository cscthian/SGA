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
                ('tipo_alumno', models.CharField(max_length=10, choices=[(b'Natural', b'Natural'), (b'Becado', b'Becado'), (b'Especial', b'Especial'), (b'Hermanos', b'Hermanos')])),
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
                ('fecha_matricula', models.DateTimeField()),
                ('periodo', models.CharField(max_length=50, verbose_name=b'tiempo duracion')),
                ('estado_matricula', models.BooleanField()),
                ('alumno', models.ForeignKey(to='matricula.Alumno')),
            ],
        ),
    ]
