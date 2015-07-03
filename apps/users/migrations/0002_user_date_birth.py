# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_birth',
            field=models.DateField(null=True, verbose_name=b'fecha de nacimiento', blank=True),
        ),
    ]
