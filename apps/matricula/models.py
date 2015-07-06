# -*- encoding: utf-8 -*-
from django.db import models
from apps.notas.models import Modulo
from django.conf import settings
from django.template.defaultfilters import slugify


class Carrera(models.Model):
    nombre_carrera = models.CharField('Nombre', max_length=50)
    siglas = models.CharField('Abrebiatura', max_length=4)
    titulo = models.CharField('Licenciatura', max_length=50)

    class meta:
        verbose_name_plural = 'Carreras'

    def __unicode__(self):
        return str(self.nombre_carrera)


class Programacion(models.Model):

    vacantes = models.PositiveIntegerField()
    inicio_labores = models.DateField()
    fin_labores = models.DateField()
    semestre = models.CharField(max_length=20)
    finalizado = models.BooleanField(default=False)

    class meta:
        verbose_name_plural = 'Programaciones'

    def __unicode__(self):
        return self.semestre


class Alumno(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    carrera_profesional = models.ForeignKey(Carrera)
    tipo_descuento = models.ForeignKey('pagos.Descuento')
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.get.full_name())
        super(Alumno, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.get_full_name()


class Matricula(models.Model):
    TURNO_CHOICES = (
        ('Maniana1', '7:00 am - 11:30 am'),
        ('Tarde', '1:00 pm - 5:30 pm'),
        ('Noche', '5:30 pm - 10:00 pm'),
    )
    alumno = models.ForeignKey(Alumno)
    modulo = models.ForeignKey(Modulo)
    turno = models.CharField(max_length=7, choices=TURNO_CHOICES)
    fecha_matricula = models.DateTimeField()
    periodo = models.CharField('tiempo duracion', max_length=50)
    estado_matricula = models.BooleanField(blank=False)
    programacion = models.ForeignKey(Programacion, null=True, blank=True)
