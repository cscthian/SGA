# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0003_alumno_user'),
        ('asistencia', '0002_auto_20150719_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargaacademica',
            name='grupo',
            field=models.ForeignKey(default=1, to='matricula.Turno'),
            preserve_default=False,
        ),
    ]
