# -*- encoding: utf-8 -*-
from django.db import models
from apps.notas.models import Modulo, Asignatura
from django.conf import settings
from django.template.defaultfilters import slugify

from datetime import date

from django.core.validators import RegexValidator


class Carrera(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    siglas = models.CharField('abrebiatura', max_length=4)
    titulo = models.CharField('licenciatura', max_length=50)

    class Meta:
        verbose_name_plural = 'Carreras'

    def __unicode__(self):
        return str(self.nombre)


class Programacion(models.Model):

    vacantes = models.PositiveIntegerField()
    inicio = models.DateField()
    fin = models.DateField()
    semestre = models.CharField(max_length=20, unique=True)
    finalizado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Programaciones'
        ordering = ['inicio']

    def __unicode__(self):
        return self.semestre


class Alumno(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    carrera_profesional = models.ForeignKey(Carrera)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.get_full_name())
        super(Alumno, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.get_full_name()


class ManagerMatricula(models.Manager):

    def matricula_pendiente(self):
        hoy = date.today()
        return self.filter(
            programacion__inicio__lte=hoy,
            programacion__fin__gte=hoy,
            completado=False,
        )


class Matricula(models.Model):
    TURNO_CHOICES = (
        ('m1', '7:00 am - 11:30 am'),
        ('m2', '8:30 am - 1:00 pm'),
        ('t1', '1:00 pm - 5:30 pm'),
        ('n1', '5:30 pm - 10:00 pm'),
    )

    alumno = models.ForeignKey(Alumno)
    modulo = models.ForeignKey(Modulo)
    turno = models.CharField(max_length=2, choices=TURNO_CHOICES)
    fecha_matricula = models.DateTimeField()
    estado_matricula = models.BooleanField(default=False)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=600,)
    completado = models.BooleanField(default=False)
    programacion = models.ForeignKey(Programacion)
    tipo_descuento = models.ForeignKey(
        'pagos.Descuento', blank=True, null=True, default=1)

    objects = ManagerMatricula()

    def __unicode__(self):
        return str(self.alumno)

class CursosCargo(models.Model):
    matricula = models.ForeignKey(Matricula)
    aisgnatura = models.ForeignKey(Asignatura)
