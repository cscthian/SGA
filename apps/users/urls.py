from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^usuario/login/$',
        views.LogIn.as_view(),
        name='login'
    ),
    url(
        r'^usuario/salir/$',
        'apps.users.views.LogOut',
        name='logout'
    ),
    url(
        r'^panel/admin/$',
        views.AdminView.as_view(),
        name='panel_admin'
    ),
    url(
        r'^panel/admin/docente$',
        views.DocenteView.as_view(),
        name='panel_docente'
    ),

]
