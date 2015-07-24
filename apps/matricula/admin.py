# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import Carrera, Programacion, Alumno, Matricula, CursosCargo
from .models import Carrera, Programacion, Alumno, Matricula, Turno

admin.site.register(Carrera)
admin.site.register(Programacion)
admin.site.register(Alumno)
admin.site.register(Matricula)
admin.site.register(CursosCargo)
admin.site.register(Turno)
