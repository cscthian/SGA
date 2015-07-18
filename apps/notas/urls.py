from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^panel/docente/$',
        views.PanelDocenteView.as_view(),
        name='panel_docente'
    ),
    url(
        r'^panel/admin/asignatura/$',
        views.PanelAsignaturaView.as_view(),
        name='panel_asignatura'
    ),
    url(
        r'^panel/admin/asignatura/agregar/$',
        views.AgregarAsignatura.as_view(),
        name='agregar_asignatura'
    ),

    url(
        r'^panel/admin/asignatura/detalle/(?P<pk>\d+)/$',
        views.DetalleAsignatura.as_view(),
        name='detalle_asignatura'
    ),
    url(
        r'^panel/admin/asignatura/modificar/(?P<pk>\d+)/$',
        views.ModificarAsignatura.as_view(),
        name='modificar_asignatura'
    ),
    url(
        r'^panel/admin/asignatura/eliminar/(?P<pk>\d+)/$',
        views.EliminarAsignatura.as_view(),
        name='eliminar_asignatura'
    ),
]
