# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aportacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concepto', models.CharField(max_length=1, choices=[(b'1', b'Matricula'), (b'2', b'Matricula Curso de Capacitacion'), (b'3', b'Subsanacion de Curso Cargo'), (b'4', b'Curso Cargo'), (b'5', b'Certificacion')])),
                ('monto', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('fecha_pago', models.DateField()),
                ('saldo', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('completado', models.BooleanField(default=False)),
                ('matricula', models.ForeignKey(to='matricula.Matricula')),
            ],
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=10)),
                ('serie', models.CharField(max_length=11)),
                ('numero', models.CharField(max_length=11)),
                ('monto_subtotal', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('monto_igv', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('monto_total', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_descuento', models.CharField(max_length=50)),
                ('porcentaje', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Comprobante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje', models.IntegerField()),
                ('monto_Descuento', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('sub_Total', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('comprobante', models.ForeignKey(to='pagos.Comprobante')),
                ('concepto', models.ForeignKey(to='pagos.Aportacion')),
            ],
        ),
        migrations.CreateModel(
            name='Estructura_Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto_matricula', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('monto_mensualidad', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('fecha_limite1', models.DateTimeField()),
                ('fecha_limite2', models.DateTimeField()),
                ('fecha_limite3', models.DateTimeField()),
                ('fecha_limite4', models.DateTimeField()),
                ('Carrera', models.ForeignKey(to='matricula.Carrera')),
                ('programacion', models.ForeignKey(to='matricula.Programacion')),
            ],
        ),
    ]
