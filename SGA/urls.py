from django.conf.urls import include, url
from django.contrib import admin

from apps.academico.views import *

urlpatterns = [
    # urls para la aplicaicon asistencia
    url(r'^', include('apps.asistencia.urls', namespace="asistencia_app")),
    # urls para la aplicaicon users
    url(r'^', include('apps.users.urls', namespace="users_app")),
    # urls para la aplicaicon asistencia
    url(r'^', include('apps.matricula.urls', namespace="matricula_app")),

    url(r'^admin/', include(admin.site.urls)),
]
