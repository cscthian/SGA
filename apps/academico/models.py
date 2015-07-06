from django.db import models

# Create your models here.

#creamos el modelo carrera profesionla
class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length = 50)
    siglas = models.CharField(max_length = 4, unique=True)
    titulo = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.nombre_carrera
#creamos el modelo Alumno
class Alumno(models.Model):
    Opcion_Sexo = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    dni=models.CharField(max_length = 8)
    nombres=models.CharField(max_length = 50)
    apellidos=models.CharField(max_length = 50)
    fecha_nacimiento = models.DateField()
    carreraTecnica=models.ForeignKey(Carrera)
    telefono=models.CharField(max_length = 50)
    sexo=models.CharField(max_length = 1, choices = Opcion_Sexo)
    direccion=models.CharField(max_length = 50)
    email=models.EmailField(max_length=50)
    foto=models.ImageField(upload_to = 'media')

    def __unicode__(self):
        return "%s %s" % (self.apellidos, self.nombres)

#creamos el modelo Docente
class Docente(models.Model):
    Opcion_Sexo = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    Tipo_Docente = (
        ('contratado', 'CONTRATADO'),
        ('nombrado', 'NOMBRADO'),
    )
    Especialidad_Docente = (
        ('administracion de bases de datos', 'ADMINISTRACION DE BASES DE DATOS'),
        ('analista de sistemas', 'ANALISTA DE SISTEMAS'),
        ('administracion de centro de computo', 'ADMINISTRACION DE CENTROS DE COMPUTO'),
        ('cursos generales', 'CURSOS GENERALES'),
    )

    dni=models.CharField(max_length = 8)
    nombres=models.CharField(max_length = 50)
    apellidos=models.CharField(max_length = 50)
    fecha_nacimiento = models.DateField()
    tipo_docente=models.CharField(max_length = 12, choices = Tipo_Docente)
    especialidad = models.CharField(max_length = 50, choices = Especialidad_Docente)
    titulo = models.CharField(max_length = 50)
    telefono=models.CharField(max_length = 50)
    sexo=models.CharField(max_length = 1, choices = Opcion_Sexo)
    direccion=models.CharField(max_length = 50)
    email=models.EmailField(max_length=50)
    foto=models.ImageField(upload_to = 'media')

    def __unicode__(self):
        return "%s %s" % (self.apellidos, self.nombres)


#reamos el modelo Modulo
class Modulo(models.Model):
    periodo_modulo = models.CharField(max_length = 6)
    carrera = models.ForeignKey(Carrera)
    modulo = models.CharField(max_length = 10)

    def __unicode__(self):
        return self.modulo

#creamos el modelo Asignatura
class Asignatura(models.Model):
    Tipo_Categoria = (
        ('obligatorio', 'obligatorio'),
        ('opcional', 'opcional'),
    )
    nombre_asignatura = models.CharField(max_length = 50)
    codigo = models.CharField(max_length = 4)   
    categoria = models.CharField(max_length = 15, choices=Tipo_Categoria)
    creditos = models.PositiveIntegerField()
    modulo = models.ForeignKey(Modulo)
    prerequisitos = models.ForeignKey('self', null=True, blank=True )
    horas_teoricas = models.PositiveIntegerField(default=0)
    horas_practicas = models.PositiveIntegerField(default=0)
    def __unicode__(self):
        return self.nombre_asignatura

#creamos el modelo Matricula
class Matricula(models.Model):
	alumno = models.ForeignKey(Alumno)
	estado_matricula = models.BooleanField()
	fecha = models.DateTimeField()

#creamos el modelo notas
class Nota(models.Model):
	nota = models.IntegerField()
	descripcion = models.CharField(max_length = 100)
	peso = models.IntegerField()


#creamos el modelo matricula detalle
class MatriculaDetalle(models.Model):
	cod_matricula = models.ForeignKey(Matricula)
	cod_asignatura = models.ForeignKey(Asignatura)
	cod_nota = models.ForeignKey(Nota)
