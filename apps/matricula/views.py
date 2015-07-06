from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy

from .forms import *

from .models import *

# Create your views here.


class Inicio(TemplateView):
    template_name = 'matricula/index.html'

#################################### CARRERAS PROFESIONALES ################
class HomeCarrera(TemplateView):
    template_name= 'carrera/index.html'

    """funcion que devolvera la lista de carreras profesionales"""
    def get_context_data(self, **kwargs):
        context = super(HomeCarrera, self).get_context_data(**kwargs)
        context['carrera'] = Carrera.objects.all().order_by('siglas')
        context['cantidad'] = context['carrera'].count()
        return context  

class AgregarCarrera(CreateView):
    form_class = CarreraForm
    template_name = 'carrera/agregar.html'
    success_url = reverse_lazy('inicio')


class DetalleCarrera(DetailView):
    template_name = 'carrera/detalle.html'
    model = Carrera

class ModificarCarrera(UpdateView):
    model = Carrera
    template_name = 'carrera/modificar.html'
    success_url = reverse_lazy('inicio')
    form_class = CarreraForm

class EliminarCarrera(DeleteView):
    template_name = 'carrera/eliminar.html'
    model = Carrera
    success_url = reverse_lazy('inicio')

################################ FIN CARRERAS PROFESIONALES #####################

############################# VIEWS PARA EL MANTENIMIENTO DE ALUMNOS ############

class HomeAlumno(TemplateView):
    template_name= 'alumno/index.html'

    """funcion que devolvera la lista de alumnos"""
    def get_context_data(self, **kwargs):
        context = super(HomeAlumno, self).get_context_data(**kwargs)
        context['alumnos'] = Alumno.objects.all().order_by('siglas')
        context['cantidad'] = context['alumnos'].count()
        return context 

class DetalleAlumno(DetailView):
    template_name = 'alumno/detalle.html'
    model = Alumno

class ModificarAlumno(UpdateView):
    model = Alumno
    template_name = 'alumno/modificar.html'
    success_url = reverse_lazy('inicio')
    form_class = AlumnoForm

class EliminarAlumno(DeleteView):
    template_name = 'alumno/eliminar.html'
    model = Alumno
    success_url = reverse_lazy('inicio')

################################## FIN VIES MANTENIMIENTO ALUMNOS

######################## vistas para MATRICULA ##########################3333
class HomeMatricula(TemplateView):
    template_name= 'matricula/index.html'

    """funcion que devolvera la lista de matriculados"""
    def get_context_data(self, **kwargs):
        context = super(HomeMatricula, self).get_context_data(**kwargs)
        context['matriculados'] = Matricula.objects.all().order_by('modulo')
        context['cantidad'] = context['matriculados'].count()
        return context  

class PreMatricula(CreateView):
    form_class = PreMatriculaForm
    template_name = 'matricula/agregar.html'
    success_url = reverse_lazy('inicio')

#funcion para verificar si el alumnos ya esta registrado
class VerificarAlumno(TemplateView):
    template_name = 'matricula/verificar_alumno.html'

    def post(self, request, *args, **kwargs):
        dni = request.POST.get('dni')
        try:
            alumno = Alumno.objects.get(dni=dni)
        except Alumno.DoesNotExist:
            return render(request, 'pre_matricula') 
        print alumno
        return render(request, 'inicio')

    def get_context_data(self, **kwargs):
        context = super(VerificarAlumno, self).get_context_data(**kwargs)
        context['form'] = DniForm
        return context

#############FIN VISTAS MATRICULA ###########################################3
