# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aportacion',
            name='completado',
        ),
        migrations.RemoveField(
            model_name='aportacion',
            name='saldo',
        ),
    ]
