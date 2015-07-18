# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursolibre', '0005_asignaturalibre_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignaturalibre',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
