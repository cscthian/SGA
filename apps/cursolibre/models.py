# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
from apps.asistencia.models import Aula, Docente, Horario

# Create your models here.


class AsignaturaLibre(models.Model):
    nombre = models.CharField('nombre del curso', max_length=50)
    costo = models.DecimalField('costo (S/.)', max_digits=6, decimal_places=2)
    mensualidad = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    duracion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='cursolibre')
    hora = models.PositiveIntegerField('total de horas lectivas')
    costo_certificado = models.DecimalField(
        'costo por certificado',
        max_digits=6,
        decimal_places=2,
    )

    def __unicode__(self):
        return self.nombre


class Ciclo(models.Model):
    MES_CHOICES = (
        ('enero', 'enero'),
        ('febrero', 'febrero'),
        ('marzo', 'marzo'),
        ('abril', 'abril'),
        ('mayo', 'mayo'),
        ('junio', 'junio'),
        ('julio', 'julio'),
        ('agosto', 'agosto'),
        ('septiembre', 'septiembre'),
        ('octubre', 'octubre'),
        ('noviembre', 'noviembre'),
        ('diciembre', 'diciembre'),
    )
    mes = models.CharField(max_length=20, choices=MES_CHOICES)
    anio = models.CharField('año', max_length=10)
    asignatura = models.ManyToManyField(AsignaturaLibre)

    def __unicode__(self):
        return "%s %s" % (self.mes, self.anio)


class Catalogo(models.Model):
    asignatura = models.ForeignKey(AsignaturaLibre)
    docente = models.ForeignKey(Docente)
    aula = models.ForeignKey(Aula)
    horario = models.ManyToManyField(Horario)


class MatriculaCursoLibre(models.Model):
    alumno = models.ForeignKey(settings.AUTH_USER_MODEL)
    asignatura = models.ForeignKey(AsignaturaLibre)
    fecha = models.DateField()
    saldo = models.DecimalField(max_digits=6, decimal_places=2, editable=False)
    ciclo = models.ForeignKey(Ciclo)

    def save(self, *args, **kwargs):
        if not self.id:
            self.saldo = self.asignatura.costo
        super(MatriculaCursoLibre, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.alumno)


class Certificado(models.Model):
    matricula = models.ForeignKey(MatriculaCursoLibre)
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateTimeField()
    estado = models.BooleanField(default=False)
