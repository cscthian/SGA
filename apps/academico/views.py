from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy


from .forms import *

from .models import Alumno, Docente, Carrera, Modulo, Asignatura, Matricula, Nota, MatriculaDetalle

# Creamos nustras vistas

""" creamos la clase que mostrara el formulario de inicio """
class Home(TemplateView):
	template_name= 'home/index.html'

	"""funcion que devolvera la lista de lumnos matriculados"""
	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['alumnos'] = Alumno.objects.all().order_by('apellidos')
		context['cantidad'] = context['alumnos'].count()
		return context	


#####################CRUD DE DOCENTES INSCRITOS ################################

class ListarDocente(TemplateView):
    template_name = 'docente/index.html'

	#creamos una funcion que devolvera la lista de alumnos
    def get_context_data(self, **kwargs):
        context = super(ListarDocente, self).get_context_data(**kwargs)
        context['docentes'] = Docente.objects.all().order_by('apellidos')
        context['cantidad'] = context['docentes'].count()
        return context

#### agregamos un docente ########
class AgregarDocente(CreateView):
	form_class = DocenteForm
	template_name = 'docente/agregar.html'
	success_url = reverse_lazy('home')

class DetalleDocente(DetailView):
	template_name = 'docente/detalle.html'
	model = Docente

class ModificarDocente(UpdateView):
    model = Docente
    template_name = 'docente/modificar.html'
    success_url = reverse_lazy('home')
    form_class = DocenteForm

class EliminarDocente(DeleteView):
    template_name = 'docente/eliminar.html'
    model = Docente
    success_url = reverse_lazy('home')

#### fin crud docentes ######

	
################################## CRUD DE ALUMNOS ################
class ListarAlumno(TemplateView):
    template_name = 'alumno/index.html'

    #creamos una funcion que devolvera la lista de alumnos
    def get_context_data(self, **kwargs):
        context = super(ListarAlumno, self).get_context_data(**kwargs)
        context['alumnos'] = Alumno.objects.all().order_by('apellidos')
        context['cantidad'] = context['alumnos'].count()
        return context

class AgregarAlumno(CreateView):
	form_class = AlumnoForm
	template_name = 'alumno/agregar.html'
	success_url = reverse_lazy('home')

class DetalleAlumno(DetailView):
	template_name = 'alumno/detalle.html'
	model = Alumno

class ModificarAlumno(UpdateView):
    model = Alumno
    template_name = 'alumno/modificar.html'
    success_url = reverse_lazy('home')
    form_class = AlumnoForm

class EliminarAlumno(DeleteView):
    template_name = 'alumno/eliminar.html'
    model = Alumno
    success_url = reverse_lazy('home')

 ################## fin de crud alumno

################################# crud de asignaturas ##################
class ListarAsignatura(TemplateView):
    template_name = 'asignatura/index.html'

    #creamos una funcion que devolvera la lista de alumnos
    def get_context_data(self, **kwargs):
        context = super(ListarAsignatura, self).get_context_data(**kwargs)
        context['asignaturas'] = Asignatura.objects.all().order_by('nombre_asignatura')
        context['cantidad'] = context['asignaturas'].count()
        return context

class AgregarAsignatura(CreateView):
	form_class = AsignaturaForm
	template_name = 'asignatura/agregar.html'
	success_url = reverse_lazy('home')


class DetalleAsignatura(DetailView):
	template_name = 'asignatura/detalle.html'
	model = Asignatura

class ModificarAsignatura(UpdateView):
    model = Asignatura
    template_name = 'asignatura/modificar.html'
    success_url = reverse_lazy('home')
    form_class = AsignaturaForm

class EliminarAsignatura(DeleteView):
    template_name = 'asignatura/eliminar.html'
    model = Asignatura
    success_url = reverse_lazy('home')

 ########### fin crud asignatura ##########

################################# crud de carreras ##################

class ListarCarrera(TemplateView):
    template_name = 'carrera/index.html'

    #creamos una funcion que devolvera la lista de alumnos
    def get_context_data(self, **kwargs):
        context = super(ListarCarrera, self).get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.all().order_by('nombre_carrera')
        context['cantidad'] = context['carreras'].count()
        return context

class AgregarCarrera(CreateView):
	form_class = CarreraForm
	template_name = 'carrera/agregar.html'
	success_url = reverse_lazy('home')


class DetalleCarrera(DetailView):
	template_name = 'carrera/detalle.html'
	model = Carrera

class ModificarCarrera(UpdateView):
    model = Carrera
    template_name = 'carrera/modificar.html'
    success_url = reverse_lazy('home')
    form_class = CarreraForm

class EliminarCarrera(DeleteView):
    template_name = 'carrera/eliminar.html'
    model = Carrera
    success_url = reverse_lazy('home')

 ################## fin crud asignaturas ###############################3333

 ##################### crud modulo #######################################
class ListarModulo(TemplateView):
    template_name = 'modulo/index.html'

    #creamos una funcion que devolvera la lista de alumnos
    def get_context_data(self, **kwargs):
        context = super(ListarModulo, self).get_context_data(**kwargs)
        context['modulos'] = Modulo.objects.all().order_by('modulo')
        context['cantidad'] = context['modulos'].count()
        return context

class AgregarModulo(CreateView):
    form_class = ModuloForm
    template_name = 'modulo/agregar.html'
    success_url = reverse_lazy('home')


class DetalleModulo(DetailView):
    template_name = 'modulo/detalle.html'
    model = Modulo

class ModificarModulo(UpdateView):
    model = Modulo
    template_name = 'modulo/modificar.html'
    success_url = reverse_lazy('home')
    form_class = CarreraForm

class EliminarModulo(DeleteView):
    template_name = 'modulo/eliminar.html'
    model = Modulo
    success_url = reverse_lazy('home')

######################33 fin crud modulo #####################################
class Matricular(TemplateView):
    template_name = 'matricula/index.html'

    def post(self, request, *args, **kwargs):
        dni = request.POST.get('dni')
        try:
            alumno = Alumno.objects.get(dni=dni)
        except Alumno.DoesNotExist:
            return render(request, 'home/index.html') 
        print alumno
        return render(request, 'matricula/agregar.html')

    def get_context_data(self, **kwargs):
        context = super(Matricular, self).get_context_data(**kwargs)
        context['form'] = DniForm
        return context

class Asistencia(TemplateView):
    template_name = 'asistencia/index.html'

class Pagos(TemplateView):
    template_name = 'pagos/index.html'

        
####################### proceso matriculas ########################################

####################### fin proceso matriculas ####################################

