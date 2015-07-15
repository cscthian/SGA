from django.contrib import admin

from .models import Aula, Docente, CargaAcademica, Horario, AsistenciaDocente
# Register your models here.

admin.site.register(Aula)
admin.site.register(Docente)
admin.site.register(CargaAcademica)
admin.site.register(Horario)
admin.site.register(AsistenciaDocente)
