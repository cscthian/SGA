# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursolibre', '0002_auto_20150717_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriculacursolibre',
            name='saldo',
            field=models.DecimalField(editable=False, max_digits=6, decimal_places=2),
        ),
    ]
