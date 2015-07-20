from django.contrib import admin
from .models import AsignaturaLibre, MatriculaCursoLibre, Ciclo, Certificado, Catalogo

# Register your models here.


admin.site.register(AsignaturaLibre)
admin.site.register(Ciclo)
admin.site.register(MatriculaCursoLibre)
admin.site.register(Certificado)
admin.site.register(Catalogo)
