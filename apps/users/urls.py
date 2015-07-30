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
        r'^panel/admin/usuario/agregar/$',
        views.AgregarAdministrador.as_view(),
        name='add_admin'
    ),
    url(
        r'^panel/admin/cajero/agregar/$',
        views.AgregarCajero.as_view(),
        name='add_cajero'
    ),
    url(
        r'^panel/admin/docente/agregar/$',
        views.AgregarDocente.as_view(),
        name='add_docente'
    ),
    url(
        r'^verificar_panel$',
        views.DistribuirPanel.as_view(),
        name='verificar_panel'
    ),
]
