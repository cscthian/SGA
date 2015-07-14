# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0003_alumno_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programacion',
            options={'ordering': ['inicio'], 'verbose_name_plural': 'Programaciones'},
        ),
        migrations.RenameField(
            model_name='programacion',
            old_name='fin_labores',
            new_name='fin',
        ),
        migrations.RenameField(
            model_name='programacion',
            old_name='inicio_labores',
            new_name='inicio',
        ),
        migrations.AddField(
            model_name='matricula',
            name='completado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matricula',
            name='saldo',
            field=models.DecimalField(default=600, max_digits=12, decimal_places=2),
        ),
    ]
