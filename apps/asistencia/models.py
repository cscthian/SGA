from django.db import models
from apps.academico.models import Docente, Asignatura


class Horario(models.Model):
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()

    class meta:
        verbose_name_plural = 'Horarios'

    def __unicode__(self):
        return str(self.dia)


class Aula(models.Model):
    AULA_CHOICES = (
        ('L', 'Laboratorio'),
        ('T', 'Teoria'),
    )
    nro_aula = models.CharField('numero de Aula', max_length=50)
    piso = models.CharField(max_length=50)
    tipo_aula = models.CharField(max_length=1, choices=AULA_CHOICES)
    capacidad = models.PositiveIntegerField(default=0)

    class meta:
        verbose_name_plural = 'Aulas'

    def __unicode__(self):
        return self.nro_aula


class CargaAcademica(models.Model):
    docente = models.ForeignKey(Docente)
    asignatura = models.ForeignKey(Asignatura)
    aula = models.ForeignKey(Aula)
    horario = models.ForeignKey(Horario)

    class meta:
        verbose_name_plural = 'Carga Academica'


class AsistenciaDocente(models.Model):
    carga_academica = models.ForeignKey(CargaAcademica)
    hora_Inicio = models.DateTimeField()
    hora_Fin = models.DateTimeField()

    class meta:
        verbose_name_plural = 'Asistencia del docente'
