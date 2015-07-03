from django.conf import settings
from django.template.defaultfilters import slugify
from django.db import models
from apps.academico.models import Asignatura


class Docente(models.Model):
    TIPO_CHOICES = (
        ('contratado', 'contratado'),
        ('nombrado', 'nombrado'),
    )
    ESPECIALIDAD_CHOICES = (
        ('1', 'administracion de bases de datos'),
        ('2', 'analista de sistemas'),
        ('3', 'administracion de centros de computo'),
        ('4', 'cursos generales'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    tipo_docente = models.CharField(max_length=12, choices=TIPO_CHOICES)
    especialidad = models.CharField(max_length=2, choices=ESPECIALIDAD_CHOICES)
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.get.full_name())
        super(Docente, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.get_full_name()


class Horario(models.Model):
    dia = models.CharField(max_length=10)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_final = models.TimeField(blank=True, null=True)

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
    hora_Inicio = models.DateTimeField(blank=True, null=True)
    hora_Fin = models.DateTimeField(blank=True, null=True)

    class meta:
        verbose_name_plural = 'Asistencia del docente'
