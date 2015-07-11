from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import DescuentoForm
from .models import Descuento


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
	template_name = 'mantenimientos/estructurapagos/estructurapagos_panel.html'
    
