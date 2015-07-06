from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^asistencia/docente/$',
        views.AsistenciaDocente.as_view(),
        name='asistencia_docente'
    ),
    url(
        r'^asistencia/alumno/$',
        views.AsistenciaDocente.as_view(),
        name='asistencia_alumno'
    ),
    url(
        r'^panel/admin/aula/$',
        views.AsistenciaDocente.as_view(),
        name='panel_aula'
    ),
    url(
        r'^panel/admin/aula/add/$',
        views.AsistenciaDocente.as_view(),
        name='agregar_aula'
    ),
    url(
        r'^panel/admin/horario/$',
        views.AsistenciaDocente.as_view(),
        name='panel_horario'
    ),
    url(
        r'^panel/admin/horario/add/$',
        views.AsistenciaDocente.as_view(),
        name='agregar_horario'
    ),
]
