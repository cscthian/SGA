# -*- encoding: utf-8 -*-
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

class ManagerModulo(models.Manager):

    def recuperar_modulo(self,kwasignatura):
        modulo = self.get(
            #filtramos el modulo por el prametyro asignatura
            asignatura=kwasignatura
        )
        print '================= hola 3 =================='
        #notas_desaprobadas.asignatura.all()
        #funcion para verificar si un alumno tiene modulo aprobado
        return modulo

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
    objects = ManagerModulo()

    class Meta:
        verbose_name_plural = 'Modulos'
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre


class ManagerNotas(models.Manager):

    def cursos_cargo(self,kwalumno):
        notas_desaprobadas = self.filter(
            #comprobamos si es menor o igual <= que lanota maxima desaprobatoria
            promedio__lte = 10,
            #filtramos la consulta por alumno
            matricula__alumno__user__username=kwalumno
        )
        #notas_desaprobadas.asignatura.all()
        #funcion para verificar si un alumno tiene modulo aprobado
        return notas_desaprobadas

    def no_aprobado(self, kwalumno):
        #verificamos si desaprobo mas de un curso
        if self.cursos_cargo(kwalumno).count() > 1:
            return True
        else:
            #el modulo es modulo aprobado
            return False

    #funcion para devolver el promedio de un alumno en especifico
    def promedio_alumno(self, kwalumno):
        notas_alumno = self.filter(
            matricula__alumno__user__username=kwalumno
            )
        #declaramos variable que devolvera el resultado
        promedio_total = 0
        #declaramos variable para sumar promedio
        suma_promedio = 0
        if notas_alumno.count()>0:
            #toamos el query notas alumno y lo recorremos para calcular el promedio
            i = 0
            #recorremos el query de notas del alumno
            while i<notas_alumno.count():
                #acumulamos los promedio en 'suma_promedio
                suma_promedio = suma_promedio + notas_alumno[i].promedio
                i+=1
            promedio_total = suma_promedio/notas_alumno.count()
        #devolvemos el promedio general del alumno     
        return promedio_total
    def notas_alumno(self,kwalumno):
        notas_alumno = self.filter(matricula__alumno__user__username=kwalumno)
        #variable que almcena cursos aprobados
        asignaturas=[]
        for notas in notas_alumno:
            if notas.promedio>10:
                asignaturas.append(notas)

        return asignaturas

class Nota(models.Model):
    matricula = models.ForeignKey('matricula.Matricula')
    docente = models.ForeignKey(Docente)
    asignatura = models.ForeignKey(Asignatura)
    nota1 = models.CharField('PP1', max_length=20, default='0')
    nota2 = models.CharField('PP2', max_length=20, default='0')
    nota3 = models.CharField('PP3', max_length=20, default='0')
    nota4 = models.CharField('PP4', max_length=20, default='0')
    promedio = models.DecimalField(max_digits=5, decimal_places=2)
    objects = ManagerNotas()

    def save(self, *args, **kwargs):
        if self.nota1>=0 and self.nota2>=0 and self.nota3>=0 and self.nota4>=0:
            self.promedio = (float(self.nota1)+float(self.nota2)+float(self.nota3)+float(self.nota4))/4
        super(Nota, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.asignatura.nombre
