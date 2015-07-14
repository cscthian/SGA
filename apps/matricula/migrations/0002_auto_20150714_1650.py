# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
        ('pagos', '0001_initial'),
        ('matricula', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='modulo',
            field=models.ForeignKey(to='notas.Modulo'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='programacion',
            field=models.ForeignKey(to='matricula.Programacion'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='carrera_profesional',
            field=models.ForeignKey(to='matricula.Carrera'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='tipo_descuento',
            field=models.ForeignKey(blank=True, to='pagos.Descuento', null=True),
        ),
    ]
