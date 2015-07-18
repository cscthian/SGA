# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursolibre', '0004_auto_20150717_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignaturalibre',
            name='descripcion',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
