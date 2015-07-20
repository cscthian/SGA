from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from apps.cursolibre.models import Ciclo

from django.utils import timezone
from datetime import datetime
from .forms import *

from .models import *
from apps.users.models import User
from apps.notas.models import *


class InicioView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        hoy = datetime.now()
        meses = [
        'enero',
        'febrero',
        'marzo',
        'abril',
        'mayo',
        'junio',
        'julio',
        'agosto',
        'septiembre',
        'octubre',
        'noviembre',
        'diciembre',
        ]
        mes = hoy.strftime('%m')
        anio = hoy.strftime('%Y')
        context = super(InicioView, self).get_context_data(**kwargs)
        context['cursomes'] = Ciclo.objects.filter(mes=meses[int(mes)-1], anio=anio)[:3]

        return context

"""MANTENIMIENTOS DE LA TABLA CARRERA"""

class HomeCarrera(TemplateView):
    '''clase que devolvera la lista de carreras profesionales'''
    template_name = 'carrera/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeCarrera, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.all().order_by('siglas')
        context['cantidad'] = context['carreras'].count()
        return context


class AgregarCarrera(CreateView):
    form_class = CarreraForm
    template_name = 'carrera/agregar.html'
    success_url = reverse_lazy('matricula_app:home_carrera')


class DetalleCarrera(DetailView):
    template_name = 'carrera/detalle.html'
    model = Carrera


class ModificarCarrera(UpdateView):
    model = Carrera
    template_name = 'carrera/modificar.html'
    success_url = reverse_lazy('matricula_app:home_carrera')
    form_class = CarreraForm


class EliminarCarrera(DeleteView):
    template_name = 'carrera/eliminar.html'
    model = Carrera
    success_url = reverse_lazy('matricula_app:home_carrera')



"""MATENIMIENTOS DE LA TABLA ALUMNO"""

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



"""MANTENIMEITOS Y PROCESOS DE LA TABLA PROGRAMACION"""

class HomeProgramacion(TemplateView):
    template_name = 'Programacion/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeProgramacion, self).get_context_data(**kwargs)
        context['programaciones'] = Programacion.objects.all().order_by('semestre')
        context['cantidad'] = context['programaciones'].count()
        return context


class AgregarProgramacion(CreateView):
    form_class = ProgramacionForm
    template_name = 'Programacion/agregar.html'
    success_url = reverse_lazy('matricula_app:home_programacion')


class DetalleProgramacion(DetailView):
    template_name = 'Programacion/detalle.html'
    model = Programacion


class ModificarProgramacion(UpdateView):
    model = Programacion
    template_name = 'Programacion/modificar.html'
    success_url = reverse_lazy('matricula_app:home_programacion')
    form_class = CarreraForm


class EliminarProgramacion(DeleteView):
    template_name = 'Programacion/eliminar.html'
    model = Carrera
    success_url = reverse_lazy('matricula_app:home_programacion')
""" FIN DE TABLA PROGRAMACION"""

################### FIN VISTAS MANTENIMIENTO ALUMNOS ##################
######################## VISTAS PARA MATRICULA ########################


class HomeMatricula(TemplateView):
    '''clase que devolvera la lista de matriculados'''
    template_name = 'matricula/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeMatricula, self).get_context_data(**kwargs)
        context['matriculas'] = Matricula.objects.all().order_by('modulo')
        context['cantidad'] = context['matriculas'].count()
        return context


class RegistrarPreMatricula(FormView):
    template_name = 'matricula/pre_matricula.html'
    form_class = PreMatriculaForm
    success_url = reverse_lazy('matricula_app:lista_matriculados')

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
        print '=============================================================='
        print modulo.pk
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

#clase para registrar la matricula de un alumno regular
class RegistrarMatricula(FormView):
    template_name = 'matricula/registrar_matricula.html'
    form_class = RegistrarMatriculaForm
    success_url = reverse_lazy('matricula_app:lista_matriculados')

    def form_valid(self, form):
       # recuperas el modulo que le corresponde
        if Nota.objects.condicion_aprobado():
            print '=============================================================='
            print Nota.objects.condicion_aprobado()
            modulo = Matricula.objects.ultimo_modulo()
        else:
            modulo = Matricula.objects.ultimo_modulo()
            print modulo

        print '=============================================================='
        turno = form.cleaned_data['turno']
        fecha = timezone.now() 

        # recuperamos el semstre actual
        programacion = Programacion.objects.all()[0]
        alumno = form.cleaned_data['alumno']

        matricula = Matricula(
            alumno=alumno,
            modulo=modulo,
            turno=turno,
            fecha_matricula=fecha,
            programacion=programacion,
        )
        matricula.save()

        nom_asig = form.cleaned_data['asignatura']
        print '====================='
        print nom_asig
        asignatura = Asignatura.objects.filter(nombre = nom_asig)
        print '**************'
        print aisgnatura
        cursocargo = CursosCargo(
            matricula = matricula,
            aisgnatura = asignatura,
            )

        return super(RegistrarMatricula, self).form_valid(form)

class MatricularAlumno(TemplateView):
    template_name = 'matricula/matricular_alumno.html'

    def post(self, request, *args, **kwargs):
        dni = request.POST.get('username')
        try:
            user = User.objects.get(username=dni)
        except User.DoesNotExist:
            return render(request,'matricula_app:pre_matricula')
        return render(request,'pagos_app:pago_matricula')

    def get_context_data(self, **kwargs):
        context = super(MatricularAlumno, self).get_context_data(**kwargs)
        context['form'] = DniForm
        return context
