# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_auto_20150723_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='especialidad',
            field=models.CharField(max_length=2, choices=[(b'1', b'administrador'), (b'2', b'economista'), (b'3', b'ingeniero'), (b'4', b'matematico'), (b'5', b'contador'), (b'6', b'analista de sistemas')]),
        ),
    ]
