# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
        ('asistencia', '0004_auto_20150715_0727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horario',
            options={'ordering': ['dia', 'hora_inicio'], 'verbose_name_plural': 'Horarios'},
        ),
        migrations.RemoveField(
            model_name='asistenciadocente',
            name='carga_academica',
        ),
        migrations.AddField(
            model_name='asistenciadocente',
            name='asignatura',
            field=models.ForeignKey(default=1, to='notas.Asignatura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asistenciadocente',
            name='docente',
            field=models.ForeignKey(default=2, to='asistencia.Docente'),
            preserve_default=False,
        ),
    ]
