# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0003_auto_20150623_1726'),
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
                ('nro_aula', models.CharField(max_length=50, verbose_name=b'Numero de Aula')),
                ('piso', models.CharField(max_length=50)),
                ('tipo_aula', models.CharField(max_length=1, choices=[(b'L', b'Laboratorio'), (b'T', b'Teoria')])),
                ('capacidad', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CargaAcademica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.RenameField(
            model_name='asignatura',
            old_name='tipo',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='asignatura',
            old_name='siglas',
            new_name='codigo',
        ),
        migrations.RemoveField(
            model_name='asignatura',
            name='carrera_profesional',
        ),
        migrations.AddField(
            model_name='asignatura',
            name='horas_practicas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='horas_teoricas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='prerequisitos',
            field=models.ForeignKey(blank=True, to='academico.Asignatura', null=True),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='creditos',
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='asignatura',
            field=models.ForeignKey(to='academico.Asignatura'),
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='aula',
            field=models.ForeignKey(to='academico.Aula'),
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='docente',
            field=models.ForeignKey(to='academico.Docente'),
        ),
        migrations.AddField(
            model_name='cargaacademica',
            name='horario',
            field=models.ForeignKey(to='academico.Horario'),
        ),
        migrations.AddField(
            model_name='asistenciadocente',
            name='carga_academica',
            field=models.ForeignKey(to='academico.CargaAcademica'),
        ),
    ]
