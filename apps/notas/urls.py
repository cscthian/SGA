from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^panel/docente/$',
        views.PanelDocenteView.as_view(),
        name='panel_docente'
    ),
]
