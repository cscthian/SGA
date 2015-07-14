from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^panel/admin/descuento/$',
        views.DescuentoView.as_view(),
        name='panel_descuento'

    ),
    url(
        r'^panel/admin/descuento/agregar/$',
        views.AgregarDescuento.as_view(),
        name='agregar_descuento'
    ),
    url(
        r'^panel/admin/descuento/detalle/(?P<pk>\d+)/$',
        views.DetalleDescuento.as_view(),
        name='detalle_descuento'
    ),
    url(
        r'^panel/admin/descuento/modificar/(?P<pk>\d+)/$',
        views.ModificarDescuento.as_view(),
        name='modificar_descuento'
    ),
    url(
        r'^panel/admin/descuento/eliminar/(?P<pk>\d+)/$',
        views.EliminarDescuento.as_view(),
        name='eliminar_descuento'
    ),


    url(
        r'^panel/admin/estructurapagos/$',
        views.EstructurapagoView.as_view(),
        name='panel_estructurapagos'
    ),
    url(
        r'^panel/admin/estructurapagos/agregar/$',
        views.AgregarEstructuraPagos.as_view(),
        name='agregar_estructurapagos'
    ),
    url(
        r'^panel/admin/estructurapagos/detalle/(?P<pk>\d+)/$',
        views.DetalleEstructuraPagos.as_view(),
        name='detalle_estructurapagos'
    ),

    url(
        r'^panel/admin/estructurapagos/modificar/(?P<pk>\d+)/$',
        views.ModificarEstructuraPagos.as_view(),
        name='modificar_estructurapagos'
    ),
    url(
        r'^panel/admin/estructurapagos/eliminar/(?P<pk>\d+)/$',
        views.EliminarEstructuraPagos.as_view(),
        name='eliminar_estructurapagos'
    ),

    url(
        r'^panel/caja/$',
        views.PanelCajaView.as_view(),
        name='panel_caja'
    ),
]
