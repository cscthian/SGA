#from django.shortcuts import render
from django.db.models import *

from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView

from django.views.generic.detail import SingleObjectMixin

from django.core.urlresolvers import reverse_lazy, reverse

from .models import Asignatura, Modulo, Nota
from .forms import AsignaturaForm, ModuloForm, NotaForm

from apps.asistencia.models import *
from apps.matricula.models import *
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


class NotaView(TemplateView):
    template_name = 'notas/notas_parciales.html'

    def get_context_data(self, **kwargs):
        context = super(NotaView, self).get_context_data(**kwargs)
        grupo_pk = kwargs.get('grupo', 0)
        asignatura_pk = kwargs.get('pk', 0)
        asignatura = Asignatura.objects.filter(pk=asignatura_pk).annotate(
            horas=F('horas_practica') + F('horas_teorica')
        ).first()
        print asignatura

        context['asignatura'] = asignatura
        return context

class MostrarCursos(TemplateView):
    template_name = 'notas/lista_cursos.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        print user
        context = super(MostrarCursos, self).get_context_data(**kwargs)
        context['cursos'] = CargaAcademica.objects.cursos_docente(user)
        return context

#clase para mostrar alumnos por curso
class AlumnosCurso(TemplateView):
    template_name = 'notas/lista_alumnos_cursos.html'
    
    def get_form_kwargs(self):
        kwargs = super(AlumnosCurso, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs.get('pk', 0),
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(AlumnosCurso, self).get_context_data(**kwargs)
        curso_pk = self.kwargs.get('pk', 0)
        print curso_pk
        curso = Asignatura.objects.get(pk=curso_pk)
        print curso
        matricula = Matricula.objects.alumnos_por_curso(curso_pk)
        context['curso'] = curso
        # self.get_form() es form_class enviamos el formulario {{ form }}
        context['matriculas'] = matricula
        return context

#metodo pra registrar notas de alumnos
class RegistrarNotas(FormView):
    form_class = NotaForm
    template_name = 'notas/registrar_nota.html'
    success_url = reverse_lazy('matricula_app:mensaje_confirmacion')

    def get_context_data(self, **kwargs):
        context = super(RegistrarNotas, self).get_context_data(**kwargs)
        alumno_pk = self.kwargs.get('alumno', 0)
        asignatura_pk = self.kwargs.get('pk',0)
        # creamos un contex matricula  
        asignatura = Asignatura.objects.filter(pk=asignatura_pk)[0]
        context['asignatura'] = asignatura
        matricula = Matricula.objects.filter(alumno=alumno_pk)[0]
        context['matricula'] = matricula
        return context

    def form_valid(self, form):
        
        user = self.request.user
        docente = Docente.objects.get(user__username=user)
        asignatura_pk = self.kwargs.get('pk',0)
        alumno_pk = self.kwargs.get('alumno', 0)
        #recuperamos el semestre actual
        sem = Programacion.objects.filter(finalizado=False)[0].semestre
        #datos para la tabla aportacion
        matricula = Matricula.objects.get(alumno=alumno_pk, programacion__semestre=sem)
        pp1 = form.cleaned_data['nota1']
        pp2 = form.cleaned_data['nota2']
        pp3 = form.cleaned_data['nota3']
        pp4 = form.cleaned_data['nota4']
        #creamos un auxiliar para calcular promedio
        aux = int(pp1) + int(pp2) + int(pp2) + int(pp3) + int(pp4)
        #calculamos promedio
        promedio = aux/4
        asignatura = Asignatura.objects.get(pk=asignatura_pk)
        nota = Nota(
            matricula=matricula,
            docente=docente,
            asignatura=asignatura,
            nota1=pp1,
            nota2=pp2,
            nota3=pp3,
            nota4=pp4,
            promedio=promedio,
        )
        nota.save()
        return super(RegistrarNotas, self).form_valid(form)

class ActualizarNota(UpdateView):
    model = Nota
    form_class = NotaForm
    template_name = 'notas/actualizar_nota.html'
    success_url = reverse_lazy('matricula_app:mensaje_confirmacion')

class VerificarNota(FormView):
    form_class = NotaForm
    template_name = 'notas/modificar_notas.html'
    success_url = reverse_lazy('matricula_app:mensaje_confirmacion')

    #sobre-escribimos la funcion que creara los context
    def get_context_data(self, **kwargs):
        context = super(VerificarNota, self).get_context_data(**kwargs)
        alumno_pk = self.kwargs.get('alumno', 0)
        asignatura_pk = self.kwargs.get('pk',0)
        # creamos un contex matricula  
        asignatura = Asignatura.objects.filter(pk=asignatura_pk)[0]
        context['asignatura'] = asignatura
        matricula = Matricula.objects.filter(alumno=alumno_pk)[0]
        context['matricula'] = matricula
        notas = Nota.objects.filter(asignatura=asignatura, matricula=matricula)[0]
        context['notas'] = notas
        return context