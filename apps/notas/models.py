from django.db import models
from django.conf import settings


# Create your models here.

class Modulo(models.Model):
    carrera_profesional = models.ForeignKey('matricula.Carrera')
    nombre_modulo = models.CharField('Nombre', max_length=50)
    
    class meta:
        verbose_name_plural = 'Alumnos'

    def __unicode__(self):
        return str(self.user.name)