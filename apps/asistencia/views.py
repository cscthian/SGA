from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin

from apps.asistencia.models import Horario, Aula

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .forms import DniForm, HorarioForm, AulaForm 
from .models import Aula


class AsistenciaDocente(SingleObjectMixin, FormView):
    template_name = 'asistencia/asistencia_docente.html'
    form_class = DniForm

    def get_success_url(self):
        print '--------------------------------------'
        return reverse('asistencia_app:asistencia_docente')

    def get(self, request, *args, **kwargs):
        print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        print self.request.POST
        self.object = None
        return super(AsistenciaDocente, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # self.object = self.request.POST.get('dni', '')
        aula = Aula.objects.get(pk=1)
        #print aula
        #self.object = aula
        #self.object = self.get_object()
        #print '####################################'
        #print self.object
        return super(AsistenciaDocente, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        print 'es validido'
        return super(AsistenciaDocente, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AsistenciaDocente, self).get_context_data(**kwargs)
        print '++++++++++++++++++++++++'
        print kwargs
        print 'el ultimo object'
        print self.object
        # print self.object
        return context



class PanelAulaView(TemplateView):
    template_name = 'aula/panel_aula.html'

    def get_context_data(self, **kwargs):
        context = super(PanelAulaView, self).get_context_data(**kwargs)
        context['aulas'] = Aula.objects.all().order_by('dia')
        context['cantidad'] = context['aulas'].count()
        return context


class DetalleAula(DetailView):
    template_name = 'aula/detalle_aula.html'
    model = Aula


class AgregarAula(CreateView):
    form_class = AulaForm
    template_name = 'aula/agregar_aula.html'
    success_url = reverse_lazy('inicio')


class ModificarAula(UpdateView):
    model = Aula
    template_name = 'aula/modificar_aula.html'
    success_url = reverse_lazy('inicio')
    form_class = AulaForm


class EliminarAula(DeleteView):
    template_name = 'aula/eliminar_aula.html'
    model = Aula
    success_url = reverse_lazy('inicio')


class PanelHorarioView(TemplateView):
    template_name = 'horario/panel_horario.html'

    def get_context_data(self, **kwargs):
        context = super(PanelHorarioView, self).get_context_data(**kwargs)
        context['horarios'] = Aula.objects.all().order_by('nombres')
        context['cantidad'] = context['aulas'].count()
        return context


class DetalleHorario(DetailView):
    template_name = 'horario/detalle_horario.html'
    model = Horario


class AgregarHorario(CreateView):
    form_class = HorarioForm
    template_name = 'horario/agregar_horario.html'
    success_url = reverse_lazy('inicio')


class ModificarHorario(UpdateView):
    model = Horario
    template_name = 'horario/modificar_horario.html'
    success_url = reverse_lazy('inicio')
    form_class = HorarioForm


class EliminarHorario(DeleteView):
    template_name = 'horario/eliminar_horario.html'
    model = Horario
    success_url = reverse_lazy('inicio')

