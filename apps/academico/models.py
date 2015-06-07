from django.db import models

# Create your models here.

#creamos el scrip de Alumnos
class Alumno(models.Model):
	apellido_paterno = models.CharField(max_length = 50)
	apellido_materno = models.CharField(max_length = 50)
	nombres = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 100)
	sexo = models.CharField(max_length = 10)
	email = models.EmailField()
	telefono = models.CharField(max_length = 10)
	dni = models.CharField(max_length = 8)

#creamos la tabla docente
class Docente(models.Model)
	apellido_paterno = models.CharField(max_length = 50)
	apellido_materno = models.CharField(max_length = 50)
	nombres = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 100)
	sexo = models.CharField(max_length = 10)
	email = models.EmailField()
	telefono = models.CharField(max_length = 10)
	dni = models.CharField(max_length = 8)
	fecha_inicio = models.DateField()
	especialidad = models.CharField(max_length = 50)