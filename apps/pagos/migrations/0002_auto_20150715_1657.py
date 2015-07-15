# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobante',
            name='monto_igv',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='monto_subtotal',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='monto_total',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='descuento',
            name='porcentaje',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='estructura_pago',
            name='monto_matricula',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='estructura_pago',
            name='monto_mensualidad',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=5),
        ),
    ]
