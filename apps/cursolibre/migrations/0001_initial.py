# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_auto_20150717_1541'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignaturaLibre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'nombre del curso')),
                ('costo', models.DecimalField(verbose_name=b'costo (S/.)', max_digits=6, decimal_places=2)),
                ('mensualidad', models.DecimalField(max_digits=6, decimal_places=2)),
                ('duracion', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to=b'cursolibre')),
                ('hora', models.PositiveIntegerField(verbose_name=b'total de horas lectivas')),
                ('costo_certificado', models.DecimalField(verbose_name=b'costo por certificado', max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.DecimalField(max_digits=6, decimal_places=2)),
                ('fecha', models.DateTimeField()),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.CharField(max_length=20, choices=[(b'enero', b'enero'), (b'febrero', b'febrero'), (b'marzo', b'marzo'), (b'abril', b'abril'), (b'mayo', b'mayo'), (b'junio', b'junio'), (b'julio', b'julio'), (b'agosto', b'agosto'), (b'septiembre', b'septiembre'), (b'octubre', b'octubre'), (b'noviembre', b'noviembre'), (b'diciembre', b'diciembre')])),
                ('anio', models.CharField(max_length=10, verbose_name=b'a\xc3\xb1o')),
                ('asignatura', models.ManyToManyField(to='cursolibre.AsignaturaLibre')),
            ],
        ),
        migrations.CreateModel(
            name='MatriculaCursoLibre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('saldo', models.DecimalField(editable=False, max_digits=5, decimal_places=2)),
                ('alumno', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('asignatura', models.ForeignKey(to='cursolibre.AsignaturaLibre')),
                ('aula', models.ForeignKey(to='asistencia.Aula')),
                ('ciclo', models.ForeignKey(to='cursolibre.Ciclo')),
                ('docente', models.ForeignKey(to='asistencia.Docente')),
                ('horario', models.ForeignKey(to='asistencia.Horario')),
            ],
        ),
        migrations.AddField(
            model_name='certificado',
            name='matricula',
            field=models.ForeignKey(to='cursolibre.MatriculaCursoLibre'),
        ),
    ]
