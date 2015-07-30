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
    url(
        r'^panel_alumno/$',
        views.AlumnoView.as_view(),
        name='panel_alumno'
    ),
    ############### FIN ALUMNO ######################
    
    ############### URL CARRERA #####################
    url(
        r'^home_carrera/$',
        views.HomeCarrera.as_view(),
        name='home_carrera'
    ),
    url(
        r'^eliminar_carrera/(?P<pk>\d+)$',
        views.EliminarCarrera.as_view(),
        name='eliminar_carrera'
    ),
    url(
        r'^modificar_carrera/(?P<pk>\d+)$',
        views.ModificarCarrera.as_view(),
        name='modificar_carrera'
    ),
    url(
        r'^detalle_carrera/(?P<pk>\d+)$',
        views.DetalleCarrera.as_view(),
        name='detalle_carrera'
    ),
    url(
        r'^agregar_carrera/$',
        views.AgregarCarrera.as_view(),
        name='agregar_carrera'
    ),
    ############### FIN CARRERA #########################
    ############### URL PROGRAMACION ####################
    url(
        r'^home_programacion$',
        views.HomeProgramacion.as_view(),
        name='home_programacion'
    ),
    url(
        r'^agregar_programacion$',
        views.AgregarProgramacion.as_view(),
        name='agregar_programacion'
    ),
    url(
        r'^detalle_programacion/(?P<pk>\d+)$',
        views.DetalleProgramacion.as_view(),
        name='detalle_programacion'
    ),
    url(
        r'^modificar_programacion/(?P<pk>\d+)$',
        views.ModificarProgramacion.as_view(),
        name='modificar_programacion'
    ),
    url(
        r'^eliminar_programacion/(?P<pk>\d+)$',
        views.EliminarProgramacion.as_view(),
        name='eliminar_programacion'
    ),
    ############### fin url programacion
    ############### URL MATRICULA #######################
    url(
        r'^pre_matricula/$',
        views.RegistrarPreMatricula.as_view(),
        name='pre_matricula'
    ),
    url(
        r'^matricular_alumno/$',
        views.MatricularAlumno.as_view(),
        name='matricular_alumno'
    ),
    url(
        r'^lista_matriculados/$',
        views.HomeMatricula.as_view(),
        name='lista_matriculados'
    ),
    url(
        r'^registrar_matricula/$',
        views.RegistrarMatricula.as_view(),
        name='registrar_matricula'
    ),
    ######### fin url Matricula #########################
    ############ url Consultas ############################
    url(
        r'^consultas/matricula_semestre/$',
        views.MatriculaPorSemestre.as_view(),
        name='matricula_semestre'
    ),
    ########### fin url Consultas #########################
]
