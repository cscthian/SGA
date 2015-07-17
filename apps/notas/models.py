from django.db import models
from django.template.defaultfilters import slugify
from apps.asistencia.models import Docente


class Asignatura(models.Model):
    TIPO_CATEGORIA_CHOICES = (
        ('obligatorio', 'obligatorio'),
        ('opcional', 'opcional'),
    )
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=15, choices=TIPO_CATEGORIA_CHOICES)
    horas_teorica = models.PositiveIntegerField(default=0)
    horas_practica = models.PositiveIntegerField(default=0)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Asignatura, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre


class Modulo(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    carrera = models.ForeignKey('matricula.Carrera')
    asignatura = models.ManyToManyField(Asignatura)
    costo = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Modulos'
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre


class ManagerNotas(models.Manager):

    def cursos_cargo(self):
        return self.filter(
            #comprobamos si es menor o igual <= que la nota maxima desaprobatoria
            promedio__lte = 10,
            #filtramos la consulta por alumno
            matricula__alumno__user__unsername = '121314'
        )
    # funcion para verificar si un alumno tiene modulo aprobado    
    def condicion_aprobado(self):
        #verificamos si desaprobo mas de un curso
        if self.cursos_cargo().count()>1:
            return False
        else:
            #el modulo es modulo aprobado
            return True

class Nota(models.Model):
    matricula = models.ForeignKey('matricula.Matricula')
    docente = models.ForeignKey(Docente)
    asignatura = models.ForeignKey(Asignatura)
    nota1 = models.CharField('PP1', max_length=20, default='--')
    nota2 = models.CharField('PP2', max_length=20, default='--')
    nota3 = models.CharField('PP3', max_length=20, default='--')
    nota4 = models.CharField('PP4', max_length=20, default='--')
    promedio = models.DecimalField(max_digits=5, decimal_places=2)
    objects = ManagerNotas()
