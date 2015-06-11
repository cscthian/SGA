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
                ('dni', models.CharField(max_length=8)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('foto', models.ImageField(upload_to=b'imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_asignatura', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=4)),
                ('tipo', models.CharField(unique=True, max_length=15)),
                ('creditos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_carrera', models.CharField(max_length=50)),
                ('siglas', models.CharField(unique=True, max_length=4)),
                ('titulo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.CharField(max_length=8)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('tipo_docente', models.CharField(max_length=12, choices=[(b'contratado', b'CONTRATADO'), (b'nombrado', b'NOMBRADO')])),
                ('especialidad', models.CharField(max_length=50, choices=[(b'administracion de bases de datos', b'ADMINISTRACION DE BASES DE DATOS'), (b'analista de sistemas', b'ANALISTA DE SISTEMAS'), (b'administracion de centro de computo', b'ADMINISTRACION DE CENTROS DE COMPUTO'), (b'cursos generales', b'CURSOS GENERALES')])),
                ('titulo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('foto', models.ImageField(upload_to=b'imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_matricula', models.BooleanField()),
                ('fecha', models.DateTimeField()),
                ('alumno', models.ForeignKey(to='academico.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='MatriculaDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_asignatura', models.ForeignKey(to='academico.Asignatura')),
                ('cod_matricula', models.ForeignKey(to='academico.Matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo_modulo', models.CharField(max_length=6)),
                ('modulo', models.CharField(max_length=10)),
                ('carrera', models.ForeignKey(to='academico.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='matriculadetalle',
            name='cod_nota',
            field=models.ForeignKey(to='academico.Nota'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='carrera_profesional',
            field=models.ForeignKey(to='academico.Carrera'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='modulo',
            field=models.ForeignKey(to='academico.Modulo'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='carreraTecnica',
            field=models.ForeignKey(to='academico.Carrera'),
        ),
    ]
