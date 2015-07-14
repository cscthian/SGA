from django.db import models
from django.template.defaultfilters import slugify
from apps.asistencia.models import Docente


class Modulo(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    carrera = models.ForeignKey('matricula.Carrera')

    class meta:
        verbose_name_plural = 'Modulos'
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre


class Asignatura(models.Model):
    TIPO_CATEGORIA_CHOICES = (
        ('obligatorio', 'obligatorio'),
        ('opcional', 'opcional'),
    )
    codigo = models.CharField(max_length=4, unique=True)
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=15, choices=TIPO_CATEGORIA_CHOICES)
    creditos = models.PositiveIntegerField(default=0)
    modulo = models.ForeignKey(Modulo)
    horas_teoricas = models.PositiveIntegerField(default=0)
    horas_practicas = models.PositiveIntegerField(default=0)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Asignatura, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class nota(models.Model):
    matricula = models.ForeignKey('matricula.Matricula')
    docente = models.ForeignKey(Docente)
    asignatura = models.ForeignKey(Asignatura)
    programacion = models.ForeignKey('matricula.Programacion')
    nota1 = models.CharField('PP1', max_length=20, default='--')
    nota2 = models.CharField('PP2', max_length=20, default='--')
    nota3 = models.CharField('PP3', max_length=20, default='--')
    nota4 = models.CharField('PP4', max_length=20, default='--')
    promedio = models.DecimalField(max_digits=5, decimal_places=2)
