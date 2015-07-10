from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^panel/admin/descuento/$',
        views.DescuentoView.as_view(),
        name='descuento_panel'

    ),
   url(
        r'^panel/admin/descuento/agregar/$',
        views.AgregarDescuento.as_view(),
        name='agregar_descuento'
    ),
    url(
        r'^panel/admin/estructurapagos/$',
        views.EstructurapagoView.as_view(),
        name='estructurapagos_panel'
    ),
]
