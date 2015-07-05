# -*- encoding: utf-8 -*-
from django.db import models
from apps.matricula.models import Programacion, Carrera, Matricula
# Create your models here.


class Comprobante(models.Model):
    tipo = models.CharField(max_length=10)
    serie = models.CharField(max_length=11)
    numero = models.CharField(max_length=11)
    monto_subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    monto_igv = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    monto_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class Descuento(models.Model):
    tipo_descuento = models.CharField(max_length=50)
    porcentaje = models.IntegerField()

    def __unicode__(self):
        return self.tipo_descuento


class Estructura_Pago(models.Model):
    monto_matricula = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    monto_mensualidad = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_limite1 = models.DateTimeField()
    fecha_limite2 = models.DateTimeField()
    fecha_limite3 = models.DateTimeField()
    fecha_limite4 = models.DateTimeField()
    programacion = models.ForeignKey(Programacion)
    Carrera = models.ForeignKey(Carrera)


class Aportacion(models.Model):
    CONCEPTO_CHOICES = (
        ('1', 'Matricula'),
        ('2', 'Matricula Curso de Capacitacion'),
        ('3', 'Subsanacion de Curso Cargo'),
        ('4', 'Curso Cargo'),
        ('5', 'Certificacion'),
    )
    concepto = models.CharField(max_length=1,choices=CONCEPTO_CHOICES)
    monto = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha_pago = models.DateField()
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    completado = models.BooleanField(default=False)
    matricula = models.ForeignKey(Matricula)

    class meta: 
    	verbose_name_plural='Aportaciones'


class Detalle_Comprobante(models.Model):

    concepto = models.ForeignKey(Aportacion)
    comprobante = models.ForeignKey(Comprobante)
    porcentaje = models.IntegerField()
    monto_Descuento = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    sub_Total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
