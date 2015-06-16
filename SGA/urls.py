from django.conf.urls import include, url
from django.contrib import admin

from apps.academico.views import *

urlpatterns = [
    url(r'^$', Home.as_view(), name = 'home'),
    ################## urls de alumno ##################################
    url(r'^listarAlumno/$', ListarAlumno.as_view(), name = 'listarAlumno'),
    url(r'^agregarAlumno/$', AgregarAlumno.as_view(), name = 'agregarAlumno'),
    url(r'^detalleAlumno/(?P<pk>\d+)$', DetalleAlumno.as_view(), name = 'detalleAlumno'),
    url(r'^modificarAlumno/(?P<pk>\d+)$', ModificarAlumno.as_view(), name = 'modificarAlumno'),
    url(r'^eliminarAlumno/(?P<pk>\d+)$', EliminarAlumno.as_view(), name = 'eliminarAlumno'),


    ################# urls docente ###################################
    url(r'^listarDocente/$', ListarDocente.as_view(), name = 'listarDocente'),
    url(r'^agregarDocente/$', AgregarDocente.as_view(), name = 'agregarDocente'),
    url(r'^detalleDocente/(?P<pk>\d+)$', DetalleDocente.as_view(), name = 'detalleDocente'),
    url(r'^modificarDocente/(?P<pk>\d+)$$', ModificarDocente.as_view(), name = 'modificarDocente'),
    url(r'^eliminarDocente/(?P<pk>\d+)$$', EliminarDocente.as_view(), name = 'eliminarDocente'),
    

    ################# urls carreras profesionales ###################################
    url(r'^listarCarrera/$', ListarCarrera.as_view(), name = 'listarCarrera'),
    url(r'^agregarCarrera/$', AgregarCarrera.as_view(), name = 'agregarCarrera'),
    url(r'^detalleCarrera/(?P<pk>\d+)$', DetalleCarrera.as_view(), name = 'detalleCarrera'),
    url(r'^modificarCarrera/(?P<pk>\d+)$$', ModificarCarrera.as_view(), name = 'modificarCarrera'),
    url(r'^eliminarCarrera/(?P<pk>\d+)$', EliminarCarrera.as_view(), name = 'eliminarCarrera'),
    

    ################# urls asignaturas ##############################################
    url(r'^listarAsignatura/$', ListarAsignatura.as_view(), name = 'listarAsignatura'),
    url(r'^agregarAsignatura/$', AgregarAsignatura.as_view(), name = 'agregarAsignatura'),
    url(r'^detalleAsignatura/(?P<pk>\d+)$', DetalleAsignatura.as_view(), name = 'detalleAsignatura'),
    url(r'^modificarAsignatura/(?P<pk>\d+)$', ModificarAsignatura.as_view(), name = 'modificarAsignatura'),
    url(r'^eliminarAsignatura/(?P<pk>\d+)$', EliminarAsignatura.as_view(), name = 'eliminarAsignatura'),
    

    ################# urls modulos ##################################################
    url(r'^listarModulo/$', ListarModulo.as_view(), name = 'listarModulo'),
    url(r'^agregarModulo/$', AgregarModulo.as_view(), name = 'agregarModulo'),
    url(r'^detalleModulo/(?P<pk>\d+)$', DetalleAsignatura.as_view(), name = 'detalleModulo'),
    url(r'^modificarModulo/(?P<pk>\d+)$', ModificarModulo.as_view(), name = 'modificarModulo'),
    url(r'^eliminarModulo/(?P<pk>\d+)$', EliminarAsignatura.as_view(), name = 'eliminarModulo'),
    

    ################# urls aulas ####################################################
    url(r'^matricular/$', Matricular.as_view(), name = 'matricular'),
    ################# fin urls Matricula ###############################
    ################ url pagos #########################################
    url(r'^pagos/$', Matricular.as_view(), name = 'pagos'),
    ################ url asistencia ###################################
    url(r'^asistencia/$', Matricular.as_view(), name = 'asistencia'),

    url(r'^admin/', include(admin.site.urls)),
]
