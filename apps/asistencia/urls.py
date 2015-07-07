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
        views.PanelAulaView.as_view(),
        name='panel_aula'
    ),
    url(
        r'^panel/admin/aula/agregar/$',
        views.AgregarAula.as_view(),
        name='agregar_aula'
    ),

    url(
        r'^panel/admin/aula/detalle/(?P<pk>\d+)/$',
        views.DetalleAula.as_view(),
        name='detalle_aula'
    ),
    url(
        r'^panel/admin/aula/modficar/(?P<pk>\d+)/$',
        views.ModificarAula.as_view(),
        name='modificar_aula'
    ),
    url(
        r'^panel/admin/aula/eliminar/(?P<pk>\d+)/$',
        views.EliminarAula.as_view(),
        name='eliminar_aula'
    ),
    url(
        r'^panel/admin/horario/$',
        views.PanelHorarioView.as_view(),
        name='panel_horario'
    ),
    url(
        r'^panel/admin/horario/add/$',
        views.AgregarHorario.as_view(),
        name='agregar_horario'
    ),
]
