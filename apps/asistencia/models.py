from django.conf import settings
from django.template.defaultfilters import slugify
from django.db import models
from datetime import date, datetime


from django.core.exceptions import ObjectDoesNotExist


class ManagerDocente(models.Manager):
    def es_docente(self, user):
        try:
            self.get(user__username=user)
        except ObjectDoesNotExist:
            return False
        return True


class Docente(models.Model):
    TIPO_CHOICES = (
        ('contratado', 'contratado'),
        ('nombrado', 'nombrado'),
    )
    ESPECIALIDAD_CHOICES = (
        ('1', 'administrador'),
        ('2', 'economista'),
        ('3', 'ingeniero'),
        ('4', 'matematico'),
        ('5', 'contador'),
        ('5', 'analista de sistemas'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    tipo_docente = models.CharField(max_length=12, choices=TIPO_CHOICES)
    especialidad = models.CharField(max_length=2, choices=ESPECIALIDAD_CHOICES)
    titulo = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    objects = ManagerDocente()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.get_full_name())
        super(Docente, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.get_full_name()


class Horario(models.Model):
    DIA_CHOICES = (
        ('lunes', 'lunes'),
        ('martes', 'martes'),
        ('miercoles', 'miercoles'),
        ('jueves', 'jueves'),
        ('viernes', 'viernes'),
        ('sabado', 'sabado'),
    )
    dia = models.CharField(max_length=10, choices=DIA_CHOICES)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_final = models.TimeField(blank=True, null=True)

    class Meta:
        ordering = ['hora_inicio']
        verbose_name_plural = 'Horarios'
        unique_together = (('dia', 'hora_inicio', 'hora_final'),)

    def __unicode__(self):
        return "%s: %s - %s" % (self.dia, str(self.hora_inicio), str(self.hora_final))


class Aula(models.Model):
    AULA_CHOICES = (
        ('L', 'laboratorio'),
        ('T', 'teoria'),
    )
    nro_aula = models.CharField('numero de Aula', max_length=50)
    piso = models.CharField(max_length=50)
    tipo_aula = models.CharField(max_length=1, choices=AULA_CHOICES)
    capacidad = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Aulas'

    def __unicode__(self):
        return self.nro_aula


class ManagerCargaAcademica(models.Manager):

    def asignatura_docente(self, docente):
        hoy = date.today()
        return self.filter(
            programacion__inicio__lte=hoy,
            programacion__fin__gte=hoy,
            docente__user__username=docente,
        ).distinct()

    

    def carga_docente(self, docente):
        dias = [
            'lunes', 'martes', 'miercoles',
            'jueves', 'viernes', 'sabado', 'domingo',
        ]
        hoy = datetime.today()
        dia = date.weekday(hoy)
        carga = self.filter(
            docente__user__username=docente,
            horario__dia=dias[dia],
            programacion__inicio__lte=hoy,
            programacion__fin__gte=hoy,
        ).distinct()
        return carga

    def tiene_carga(self, docente):
        carga = self.carga_docente(docente)

        if carga:
            return True
        else:
            return False


class CargaAcademica(models.Model):
    docente = models.ForeignKey(Docente)
    asignatura = models.ForeignKey('notas.Asignatura')
    aula = models.ForeignKey(Aula)
    horario = models.ManyToManyField(Horario)
    grupo = models.ForeignKey('matricula.Turno')
    programacion = models.ForeignKey('matricula.Programacion')

    objects = ManagerCargaAcademica()

    class Meta:
        verbose_name_plural = 'Carga academica'

    def __unicode__(self):
        return "%s %s " % (str(self.docente), str(self.asignatura))


class AsistenciaDocente(models.Model):
    docente = models.ForeignKey(Docente)
    asignatura = models.ForeignKey('notas.Asignatura')
    programacion = models.ForeignKey('matricula.Programacion')
    hora_Inicio = models.DateTimeField(blank=True, null=True)
    hora_Fin = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Asistencia del docente'


class AsistenciaAlumno(models.Model):
    docente = models.ForeignKey(Docente)
    matricula = models.ForeignKey('matricula.Matricula')
    asignatura = models.ForeignKey('notas.Asignatura')
    estado = models.BooleanField(default=False)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Asistencia del alumno'
