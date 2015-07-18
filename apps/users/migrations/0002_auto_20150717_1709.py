# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'users', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name=b'tipo de usuario', choices=[(b'1', b'alumno'), (b'2', b'docente'), (b'3', b'cajero'), (b'4', b'administrador'), (b'5', b'alumnocursolibre')]),
        ),
    ]
