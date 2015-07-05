# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.CharField(max_length=10),
        ),
    ]
