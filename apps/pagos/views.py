from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import *
from .models import Descuento


class DescuentoView(TemplateView):
	template_name = 'mantenimientos/descuento/panel_descuento.html'

	def get_context_data(self, **kwargs):
	    context = super(DescuentoView, self).get_context_data(**kwargs)
	    context['descuentos'] = Descuento.objects.all()
	    context['cantidad'] = context['descuentos'].count()
	    return context


class EstructurapagoView(TemplateView):
	template_name = 'mantenimientos/estructurapagos/estructurapagos_panel.html'
    
class AgregarDescuento(CreateView):
    form_class = DescuentoForm
    template_name = 'mantenimientos/descuento/agregar.html'
    success_url = reverse_lazy('inicio')
