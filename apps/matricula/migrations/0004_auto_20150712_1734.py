# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0003_alumno_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='periodo',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='tipo_descuento',
            field=models.ForeignKey(blank=True, to='pagos.Descuento', null=True),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='estado_matricula',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='programacion',
            field=models.ForeignKey(to='matricula.Programacion'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='turno',
            field=models.CharField(max_length=7, choices=[(b'Maniana1', b'7:00 am - 11:30 am'), (b'Maniana2', b'8:30 am - 1:00 pm'), (b'Tarde', b'1:00 pm - 5:30 pm'), (b'Noche', b'5:30 pm - 10:00 pm')]),
        ),
    ]
