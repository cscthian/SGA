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
        r'^asistencia/administrativo/$',
        views.AsistenciaDocente.as_view(),
        name='asistencia_administrativo'
    ),
]
