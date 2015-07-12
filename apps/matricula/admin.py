from django.contrib import admin

from .models import Carrera, Programacion, Alumno

admin.site.register(Carrera)
admin.site.register(Programacion)
admin.site.register(Alumno)
