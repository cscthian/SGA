# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='tipo',
            field=models.CharField(max_length=15, choices=[(b'obligatorio', b'OBLIGATORIO'), (b'opcional', b'OPCIONAL')]),
        ),
    ]
