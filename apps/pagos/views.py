from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import DescuentoForm, EstructuraPagosForm, ComprobanteForm
from .models import Descuento, Estructura_Pago, Comprobante


class DescuentoView(TemplateView):
    template_name = 'mantenimientos/descuento/panel_descuento.html'

    def get_context_data(self, **kwargs):
        context = super(DescuentoView, self).get_context_data(**kwargs)
        context['descuentos'] = Descuento.objects.all()
        context['cantidad'] = context['descuentos'].count()
        return context


class DetalleDescuento(DetailView):
    template_name = 'mantenimientos/descuento/detalle_descuento.html'
    model = Descuento


class AgregarDescuento(CreateView):
    form_class = DescuentoForm
    template_name = 'mantenimientos/descuento/agregar_descuento.html'
    success_url = reverse_lazy('pagos_app:panel_descuento')


class ModificarDescuento(UpdateView):
    model = Descuento
    template_name = 'mantenimientos/descuento/modificar_descuento.html'
    success_url = reverse_lazy('pagos_app:panel_descuento')
    form_class = DescuentoForm


class EliminarDescuento(DeleteView):
    template_name = 'mantenimientos/descuento/eliminar_descuento.html'
    model = Descuento
    success_url = reverse_lazy('pagos_app:panel_descuento')



class EstructurapagoView(TemplateView):
    template_name = 'mantenimientos/estructurapagos/panel_estructurapagos.html'

    def get_context_data(self, **kwargs):
        context = super(EstructurapagoView, self).get_context_data(**kwargs)
        context['EstructuraPagos'] = Estructura_Pago.objects.all()
        context['cantidad'] = context['EstructuraPagos'].count()
        return context
    
class DetalleEstructuraPagos(DetailView):
    template_name = 'mantenimientos/estructurapagos/detalle_estructurapagos.html'
    model = Estructura_Pago


class AgregarEstructuraPagos(CreateView):
    form_class = EstructuraPagosForm
    template_name = 'mantenimientos/estructurapagos/agregar_estructurapagos.html'
    success_url = reverse_lazy('pagos_app:panel_estructurapagos')


class ModificarEstructuraPagos(UpdateView):
    model = Estructura_Pago
    template_name = 'mantenimientos/estructurapagos/modificar_estructurapagos.html'
    success_url = reverse_lazy('pagos_app:panel_estructurapagos')
    form_class = EstructuraPagosForm


class EliminarEstructuraPagos(DeleteView):
    template_name = 'mantenimientos/estructurapagos/eliminar_estructurapagos.html'
    model = Estructura_Pago
    success_url = reverse_lazy('pagos_app:panel_estructurapagos')


class ComprobanteView(TemplateView):
    template_name = 'procesos/panel_comprobante.html'

    def get_context_data(self, **kwargs):
        context = super(ComprobanteView, self).get_context_data(**kwargs)
        context['Comprobante'] = Comprobante.objects.all()
        context['cantidad'] = context['Comprobante'].count()
        return context
