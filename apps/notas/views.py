#from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,CreateView,UpdateView,DeleteView
#from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from .models import Asignatura , Modulo
from django.core.urlresolvers import reverse_lazy, reverse
#from django.http import HttpResponseRedirect
from .forms import AsignaturaForm, ModuloForm
# Create your views here.


class PanelDocenteView(TemplateView):
    template_name = 'panel_docente/panel.html'


class PanelAsignaturaView(TemplateView):
    template_name = 'mantenimientos/asignatura/panel_asignatura.html'

    def get_context_data(self, **kwargs):
        context = super(PanelAsignaturaView, self).get_context_data(**kwargs)
        context['asignaturas'] = Asignatura.objects.all().order_by('codigo')
        context['cantidad'] = context['asignaturas'].count()
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


class PanelModuloView(TemplateView):
    template_name = 'mantenimientos/modulo/panel_modulo.html'

    def get_context_data(self, **kwargs):
        context = super(PanelModuloView, self).get_context_data(**kwargs)
        context['modulos'] = Modulo.objects.all().order_by('nombre')
        context['nro'] = context['modulos'].count()
        return context


class DetalleModulo(DetailView):
    template_name = 'mantenimientos/modulo/detalle_modulo.html'
    model = Modulo


class AgregarModulo(CreateView):
    form_class = ModuloForm
    template_name = 'mantenimientos/modulo/agregar_modulo.html'
    success_url = reverse_lazy('notas_app:panel_modulo')


class ModificarModulo(UpdateView):
    model = Modulo
    form_class = ModuloForm
    template_name = 'mantenimientos/modulo/modificar_modulo.html'
    success_url = reverse_lazy('notas_app:panel_modulo')


class EliminarModulo(DeleteView):
    template_name = 'mantenimientos/modulo/eliminar_modulo.html'
    model = Modulo
    success_url = reverse_lazy('notas_app:panel_modulo')
