# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Modulo, Asignatura, Nota
# Register your models here.

admin.site.register(Modulo)
admin.site.register(Asignatura)
admin.site.register(Nota)
