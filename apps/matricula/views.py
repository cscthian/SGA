from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy

from django.utils import timezone
import datetime
from .forms import *

from .models import *
from apps.users.models import User


class InicioView(TemplateView):
    template_name = 'home/index.html'


class HomeCarrera(TemplateView):
    '''clase que devolvera la lista de carreras profesionales'''
    template_name = 'carrera/index.html'

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


class HomeAlumno(TemplateView):
    '''clase que devolvera la lista de alumnos'''
    template_name = 'alumno/index.html'

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

################### FIN VISTAS MANTENIMIENTO ALUMNOS ##################
######################## VISTAS PARA MATRICULA ########################


class HomeMatricula(TemplateView):
    '''clase que devolvera la lista de matriculados'''
    template_name = 'matricula/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeMatricula, self).get_context_data(**kwargs)
        context['matriculados'] = Matricula.objects.all().order_by('modulo')
        context['cantidad'] = context['matriculados'].count()
        return context


class RegistrarPreMatricula(FormView):
    template_name = 'matricula/pre_matricula.html'
    form_class = PreMatriculaForm
    success_url = reverse_lazy('asistencia_app:panel_aula')

    def form_valid(self, form):
        dni = form.cleaned_data['username']
        nombres = form.cleaned_data['first_name']
        apellidos = form.cleaned_data['last_name']
        telefono = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        sexo = form.cleaned_data['gender']
        avatar = form.cleaned_data['avatar']
        direccion = form.cleaned_data['address']
        fecha_nacimineto = form.cleaned_data['date_birth']
        tipo_user = '1'

        password = form.cleaned_data['username']

        user = User.objects.create_user(
            username=dni,
            first_name=nombres,
            last_name=apellidos,
            phone=telefono,
            email=email,
            gender=sexo,
            avatar=avatar,
            address=direccion,
            date_birth=fecha_nacimineto,
            type_user=tipo_user,
            password=password,
        )
        user.save()

        carrera = form.cleaned_data['carrera_profesional']

        # ---regitro del alumno
        alumno = Alumno(user=user, carrera_profesional=carrera)
        alumno.save()

        # ---registro de una pre-matricula

        # recuperas el primer modulo de la carrera
        modulo = Modulo.objects.filter(carrera__nombre=carrera, nombre='1')[0]
        turno = form.cleaned_data['turno']
        fecha = timezone.now()

        # recuperamos el semstre actual
        programacion = Programacion.objects.all()[0]

        pre_matricula = Matricula(
            alumno=alumno,
            modulo=modulo,
            turno=turno,
            fecha_matricula=fecha,
            programacion=programacion,
        )
        pre_matricula.save()

        return super(RegistrarPreMatricula, self).form_valid(form)


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
