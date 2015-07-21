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
        #consulta los cursos del modulo 1
        #eturn self.filter(nambre='1', asignatura

class Modulo(models.Model):
    MODULO_CHOICES = (
        ('1', 'Modulo 1'),
        ('2', 'Modulo 2'),
        ('3', 'Modulo 3'),
        ('4', 'Modulo 4'),
        ('5', 'Modulo 5'),
        ('6', 'Modulo 6'),
    )
    nombre = models.CharField('Nombre', max_length=2, choices=MODULO_CHOICES)
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
        notas_desaprobadas = self.filter(
            #comprobamos si es menor o igual <= que lanota maxima desaprobatoria
            promedio__lte = 10,
            #filtramos la consulta por alumno
            matricula__alumno__user__username = '1111'
        )
        #notas_desaprobadas.asignatura.all()
        #funcion para verificar si un alumno tiene modulo aprobado
        return notas_desaprobadas

    def condicion_aprobado(self):
        #verificamos si desaprobo mas de un curso
        if self.cursos_cargo().count() > 1:
            return False
        else:
            #el modulo es modulo aprobado
            return True

    #funcion para devolver el promedio de un alumno en especifico
    def promedio_alumno(self):
        notas_alumno = self.filter(
            matricula__alumno__user__username = '1111'
            )
        #toamos el query notas alumno y lo recorremos para calcular el promedio
        i = 0
        #declaramos una variable que sumara los promedios
        suma_promedio = 0
        #recorremos el query de notas del alumno
        while i<notas_alumno.count():
            #acumulamos los promedio en 'suma_promedio
             suma_promedio = suma_promedio + notas_alumno[0].promedio
             i+=1

        #devolvemos el promedio general del alumno     
        return suma_promedio/notas_alumno.count()

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

    def __unicode__(self):
        return self.asignatura.nombre
