from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # urls para la aplicacion asistencia
    url(r'^', include('apps.asistencia.urls', namespace="asistencia_app")),
    # urls para la aplicacion users
    url(r'^', include('apps.users.urls', namespace="users_app")),
    # urls para la aplicacion Matricula
    url(r'^', include('apps.matricula.urls', namespace="matricula_app")),
    # urls para la aplicacion de pagos
    url(r'^', include('apps.pagos.urls', namespace="pagos_app")),
    # urls para la aplicacion de notas
    url(r'^', include('apps.notas.urls', namespace="notas_app")),
    # urls para la aplicacion de notas
    url(r'^', include('apps.cursolibre.urls', namespace="cursolibre_app")),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    ]
