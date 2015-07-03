from django.db import models
from apps.notas.models import Modulo
from django.conf import settings

class Carrera(models.Model):
    nombre_carrera = models.CharField('Nombre', max_length=50)
    siglas = models.CharField('Abrebiatura', max_length=4)
    titulo = models.CharField('Licenciatura', max_length=50)

    class meta:
        verbose_name_plural = 'Carreras'

    def __unicode__(self):
        return str(self.nombre_carrera)

        
class Alumno(models.Model):
    ALUMNO_CHOICES = (
        ('Natural', 'Natural'),
        ('Becado', 'Becado'),
        ('Especial', 'Especial'),
        ('Hermanos', 'Hermanos'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    tipo_alumno = models.CharField(max_length=10, choices=ALUMNO_CHOICES)
    carrera_profesional = models.ForeignKey(Carrera)

    class meta:
        verbose_name_plural = 'Alumnos'

    def __unicode__(self):
        return str(self.user.name)
        

class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno)
    modulo = models.ForeignKey(Modulo)
    fecha_matricula = models.DateTimeField()
    periodo = models.CharField('tiempo duracion', max_length=50)
    estado_matricula = models.BooleanField(blank=False)