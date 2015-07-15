# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0003_alumno_user'),
        ('asistencia', '0003_auto_20150715_0636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asistenciaalumno',
            options={'verbose_name_plural': 'Asistencia del alumno'},
        ),
        migrations.AlterModelOptions(
            name='asistenciadocente',
            options={'verbose_name_plural': 'Asistencia del docente'},
        ),
        migrations.RemoveField(
            model_name='asistenciaalumno',
            name='hora_Fin',
        ),
        migrations.AddField(
            model_name='asistenciadocente',
            name='programacion',
            field=models.ForeignKey(default=1, to='matricula.Programacion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.CharField(max_length=10, choices=[(b'lunes', b'lunes'), (b'martes', b'martes'), (b'miercoles', b'miercoles'), (b'jueves', b'jueves'), (b'viernes', b'viernes'), (b'sabado', b'sabado')]),
        ),
        migrations.AlterUniqueTogether(
            name='horario',
            unique_together=set([('dia', 'hora_inicio', 'hora_final')]),
        ),
    ]
