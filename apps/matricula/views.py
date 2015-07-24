from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.edit import FormMixin, FormView
from django.core.urlresolvers import reverse_lazy
from apps.cursolibre.models import Ciclo

from django.utils import timezone
from datetime import datetime
from .forms import *
from braces.views import LoginRequiredMixin

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
        #cantidad de imagenes en la portada
        context['cursomes'] = Ciclo.objects.filter(mes=meses[int(mes)-1], anio=anio)[:5]

        return context

"""MANTENIMIENTOS DE LA TABLA CARRERA"""

class HomeCarrera(LoginRequiredMixin, TemplateView):
    '''clase que devolvera la lista de carreras profesionales'''
    template_name = 'carrera/index.html'
    login_url = reverse_lazy('users_app:login')

    def get_context_data(self, **kwargs):
        context = super(HomeCarrera, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.all().order_by('siglas')
        context['cantidad'] = context['carreras'].count()
        return context


class AgregarCarrera(LoginRequiredMixin, CreateView):
    form_class = CarreraForm
    template_name = 'carrera/agregar.html'
    success_url = reverse_lazy('matricula_app:home_carrera')
    login_url = reverse_lazy('users_app:login')


class DetalleCarrera(LoginRequiredMixin, DetailView):
    template_name = 'carrera/detalle.html'
    login_url = reverse_lazy('users_app:login')
    model = Carrera


class ModificarCarrera(LoginRequiredMixin, UpdateView):
    model = Carrera
    template_name = 'carrera/modificar.html'
    success_url = reverse_lazy('matricula_app:home_carrera')
    login_url = reverse_lazy('users_app:login')
    form_class = CarreraForm


class EliminarCarrera(LoginRequiredMixin, DeleteView):
    template_name = 'carrera/eliminar.html'
    model = Carrera
    success_url = reverse_lazy('matricula_app:home_carrera')
    login_url = reverse_lazy('users_app:login')



"""MATENIMIENTOS DE LA TABLA ALUMNO"""

class HomeAlumno(LoginRequiredMixin, TemplateView):
    '''clase que devolvera la lista de alumnos'''
    template_name = 'alumno/index.html'
    login_url = reverse_lazy('users_app:login')

    def get_context_data(self, **kwargs):
        context = super(HomeAlumno, self).get_context_data(**kwargs)
        context['alumnos'] = Alumno.objects.all().order_by('siglas')
        context['cantidad'] = context['alumnos'].count()
        return context


class DetalleAlumno(LoginRequiredMixin, DetailView):
    template_name = 'alumno/detalle.html'
    login_url = reverse_lazy('users_app:login')
    model = Alumno


class ModificarAlumno(LoginRequiredMixin, UpdateView):
    model = Alumno
    template_name = 'alumno/modificar.html'
    login_url = reverse_lazy('users_app:login')
    success_url = reverse_lazy('inicio')
    form_class = AlumnoForm


class EliminarAlumno(LoginRequiredMixin, DeleteView):
    template_name = 'alumno/eliminar.html'
    login_url = reverse_lazy('users_app:login')
    model = Alumno
    success_url = reverse_lazy('inicio')



"""MANTENIMEITOS Y PROCESOS DE LA TABLA PROGRAMACION"""

class HomeProgramacion(LoginRequiredMixin, TemplateView):
    template_name = 'Programacion/index.html'
    login_url = reverse_lazy('users_app:login')

    def get_context_data(self, **kwargs):
        context = super(HomeProgramacion, self).get_context_data(**kwargs)
        context['programaciones'] = Programacion.objects.all().order_by('semestre')
        context['cantidad'] = context['programaciones'].count()
        return context


class AgregarProgramacion(LoginRequiredMixin, CreateView):
    form_class = ProgramacionForm
    template_name = 'Programacion/agregar.html'
    login_url = reverse_lazy('users_app:login')
    success_url = reverse_lazy('matricula_app:home_programacion')


class DetalleProgramacion(LoginRequiredMixin, DetailView):
    template_name = 'Programacion/detalle.html'
    login_url = reverse_lazy('users_app:login')
    model = Programacion


class ModificarProgramacion(LoginRequiredMixin, UpdateView):
    model = Programacion
    template_name = 'Programacion/modificar.html'
    success_url = reverse_lazy('matricula_app:home_programacion')
    login_url = reverse_lazy('users_app:login')
    form_class = CarreraForm


class EliminarProgramacion(LoginRequiredMixin, DeleteView):
    template_name = 'Programacion/eliminar.html'
    login_url = reverse_lazy('users_app:login')
    model = Carrera
    success_url = reverse_lazy('matricula_app:home_programacion')
""" FIN DE TABLA PROGRAMACION"""

################### FIN VISTAS MANTENIMIENTO ALUMNOS ##################
######################## VISTAS PARA MATRICULA ########################


class HomeMatricula(LoginRequiredMixin, ListView):
    '''clase que devolvera la lista de matriculados'''
    template_name = 'matricula/index.html'
    login_url = reverse_lazy('users_app:login')
    paginate_by = 20

    def get_queryset(self):
        # se crea la variable objeto
        self.matriculados = Matricula.objects.all().order_by('modulo')
        return self.matriculados

    def get_context_data(self, **kwargs):
        context = super(HomeMatricula, self).get_context_data(**kwargs)
        context['cantidad'] = self.matriculados.count()
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
            password=dni,
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
        tamanio = Programacion.objects.all().count()
        programacion = Programacion.objects.all()[tamanio-1]

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
class RegistrarMatricula(LoginRequiredMixin, FormView):
    template_name = 'matricula/registrar_matricula.html'
    login_url = reverse_lazy('users_app:login')
    form_class = RegistrarMatriculaForm
    success_url = reverse_lazy('matricula_app:lista_matriculados')

    def get_context_data(self, **kwargs):
        context = super(RegistrarMatricula, self).get_context_data(**kwargs)
        user = self.request.user
        matricula = Matricula.objects.get(alumno__user__username=user)
        context['matricula'] = matricula
        modulo = Matricula.objects.ultimo_modulo(user)
        context['modulo'] = modulo
        promedio = Nota.objects.promedio_alumno(user)
        context['promedio'] = promedio
        return context

    def get_form_kwargs(self):
        kwargs = super(RegistrarMatricula, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs

    def form_valid(self, form):
       # recuperas el modulo que le corresponde
        usuario = self.request.user
        if Nota.objects.condicion_aprobado(usuario):
            modulo = Matricula.objects.ultimo_modulo(usuario)
            print ' ======== modulo 1 ========='
            print modulo
        else: 
            #generamos el nuevo modulo
            nuevo_modulo = int(Matricula.objects.ultimo_modulo(usuario)) + 1
            # recuperamos el nuevo modulo
            modulo = Modulo.objects.get(nombre = nuevo_modulo)
            print ' ======== modulo 1 ========='
            print modulo

        turno = form.cleaned_data['turno']
        fecha = timezone.now() 

        # recuperamos el semstre actual
        programacion = Programacion.objects.all()[0]
        alumno = Alumno.objects.get(user__username=usuario)

        matricula = Matricula(
            alumno=alumno,
            modulo=modulo,
            turno=turno,
            fecha_matricula=fecha,
            programacion=programacion,
        )
        matricula.save()

        asignaturas = form.cleaned_data['asignatura']

        if asignaturas.count()>0: 
            for asignatura in asignaturas: 
                cursocargo = CursosCargo(
                    matricula = matricula,
                    aisgnatura = asignatura.asignatura,
                    )
                cursocargo.save()
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


""" ================ views para consultas ========================="""

class MatriculaPorSemestre(LoginRequiredMixin, TemplateView):
    '''clase que devolvera la lista de matriculados e un semestre'''
    template_name = 'consultas/index.html'
    login_url = reverse_lazy('users_app:login')

    def get_context_data(self, **kwargs):
        context = super(MatriculaPorSemestre, self).get_context_data(**kwargs)
        context['matriculas'] = Matricula.objects.all().order_by('modulo')
        context['cantidad'] = context['matriculas'].count()
        return context