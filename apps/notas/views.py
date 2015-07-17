from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,CreateView,UpdateView,DeleteView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from .models import Asignatura
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import AsignaturaForm
# Create your views here.


class PanelDocenteView(TemplateView):
    template_name = 'panel_docente/panel.html'

class PanelAsignaturaView(TemplateView):
    template_name = 'mantenimientos/asignatura/panel_asignatura.html'

    def get_context_data(self, **kwargs):
        context = super(PanelAsignaturaView, self).get_context_data(**kwargs)
        context['asignatura'] = Asignatura.objects.all().order_by('nro_asignatura')
        context['cantidad'] = context['asignatura'].count()
        return context

class DetalleAsignatura(DetailView):
    template_name = 'mantenimientos/asignatura/detalle_asignatura.html'
    model = Asignatura


class AgregarAsignatura(CreateView):
    form_class = AsignaturaForm
    template_name = 'mantenimientos/asignatura/agregar_asignatura.html'
    success_url = reverse_lazy('notas_app:panel_asignatura')


class ModificarAsignatura(UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'mantenimientos/asignatura/modificar_asignatura.html'
    success_url = reverse_lazy('notas_app:panel_asignatura')

class EliminarAsignatura(DeleteView):
    template_name = 'mantenimientos/asignatura/eliminar_asignatura.html'
    model = Asignatura
    success_url = reverse_lazy('notas_app:panel_asignatura')
