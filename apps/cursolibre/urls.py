from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^curso/libre/(?P<pk>\d+)/$',
        views.MatriculaCurso.as_view(),
        name='matricula_cursolibre'
    ),
    url(
        r'^curso/libre/matricula/$',
        views.PreMatriculaCurso.as_view(),
        name='pre_cursolibre'
    ),
]
