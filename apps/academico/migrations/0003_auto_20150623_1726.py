# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0002_auto_20150614_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='foto',
            field=models.ImageField(upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='foto',
            field=models.ImageField(upload_to=b'media'),
        ),
    ]
