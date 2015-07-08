from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.InicioView.as_view(),
        name='inicio'
    ),
    ############### URL ALUMNO#########################
    url(
        r'^home_alumno/$',
        views.HomeAlumno.as_view(),
        name='home_alumno'
    ),
    url(
        r'^eliminar_alumno/$',
        views.EliminarAlumno.as_view(),
        name='eliminar_alumno'
    ),

    url(
        r'^modificar_alumno/$',
        views.ModificarAlumno.as_view(),
        name='modificar_alumno'
    ),
    url(
        r'^detalle_alumno/$',
        views.DetalleAlumno.as_view(),
        name='detalle_alumno'
    ),
    ############### FIN ALUMNO ######################
    ############### URL CARRERA #####################
    url(
        r'^home_carrera/$',
        views.HomeCarrera.as_view(),
        name='home_carrera'
    ),
    url(
        r'^eliminar_carrera/$',
        views.EliminarCarrera.as_view(),
        name='eliminar_carrera'
    ),
    url(
        r'^modificar_carrera/$',
        views.ModificarCarrera.as_view(),
        name='modificar_carrera'
    ),
    url(
        r'^detalle_carrera/$',
        views.DetalleCarrera.as_view(),
        name='detalle_carrera'
    ),
    url(
        r'^agregar_carrera/$',
        views.AgregarCarrera.as_view(),
        name='agregar_carrera'
    ),
    ############### FIN CARRERA #########################
    ############### URL MATRICULA #######################
    url(
        r'^pre_matricula/$',
        views.PreMatricula.as_view(),
        name='pre_matricula'
    ),
    url(
        r'^verificar_alumno/$',
        views.VerificarAlumno.as_view(),
        name='verificar_alumno'
    ),
]
