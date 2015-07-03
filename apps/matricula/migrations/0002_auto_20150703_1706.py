# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notas', '0001_initial'),
        ('matricula', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='modulo',
            field=models.ForeignKey(to='notas.Modulo'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='carrera_profesional',
            field=models.ForeignKey(to='matricula.Carrera'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
