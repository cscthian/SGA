from django.db import models
from django.template.defaultfilters import slugify


class Modulo(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    carrera_profesional = models.ForeignKey('matricula.Carrera')

    class meta:
        verbose_name_plural = 'Modulos'

    def __unicode__(self):
        return self.nombre_modulo


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
            self.slug = slugify(self.user.get.full_name())
        super(Asignatura, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre
