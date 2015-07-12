from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin

from .models import Horario, Aula, Docente
from apps.users.models import User

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .forms import DniForm, HorarioForm, AulaForm, DocenteForm


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
        context['aulas'] = Aula.objects.all().order_by('nro_aula')
        context['cantidad'] = context['aulas'].count()
        return context


class DetalleAula(DetailView):
    template_name = 'aula/detalle_aula.html'
    model = Aula


class AgregarAula(CreateView):
    form_class = AulaForm
    template_name = 'aula/agregar_aula.html'
    success_url = reverse_lazy('asistencia_app:panel_aula')


class ModificarAula(UpdateView):
    model = Aula
    template_name = 'aula/modificar_aula.html'
    success_url = reverse_lazy('asistencia_app:panel_aula')
    form_class = AulaForm


class EliminarAula(DeleteView):
    template_name = 'aula/eliminar_aula.html'
    model = Aula
    success_url = reverse_lazy('asistencia_app:panel_aula')


class PanelHorarioView(TemplateView):
    template_name = 'horario/panel_horario.html'

    def get_context_data(self, **kwargs):
        context = super(PanelHorarioView, self).get_context_data(**kwargs)
        context['horarios'] = Horario.objects.all().order_by('dia')
        context['cantidad'] = context['horarios'].count()
        return context


class DetalleHorario(DetailView):
    template_name = 'horario/detalle_horario.html'
    model = Horario


class AgregarHorario(CreateView):
    form_class = HorarioForm
    template_name = 'horario/agregar_horario.html'
    success_url = reverse_lazy('asistencia_app:panel_horario')


class ModificarHorario(UpdateView):
    model = Horario
    template_name = 'horario/modificar_horario.html'
    success_url = reverse_lazy('asistencia_app:panel_horario')
    form_class = HorarioForm


class EliminarHorario(DeleteView):
    template_name = 'horario/eliminar_horario.html'
    model = Horario
    success_url = reverse_lazy('asistencia_app:panel_horario')


class PanelDocenteView(TemplateView):
    template_name = 'docente/panel_docente.html'

    def get_context_data(self, **kwargs):
        context = super(PanelDocenteView, self).get_context_data(**kwargs)
        context['docentes'] = Docente.objects.all()
        context['cantidad'] = context['docentes'].count()
        return context


class AgregarDocente(FormView):
    template_name = 'docente/agregar_docente.html'
    form_class = DocenteForm
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
        tipo_user = '2'
        password = form.cleaned_data['password1']

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

        tipo_docente = form.cleaned_data['tipo_docente']
        especialidad = form.cleaned_data['especialidad']
        titulo = form.cleaned_data['titulo']

        Docente.objects.create(
            user=user,
            tipo_docente=tipo_docente,
            especialidad=especialidad,
            titulo=titulo,
        )

        # user = form.save()
        # user.type_user = '4'
        # user.set_password(form.cleaned_data['password1'])
        # user.save()
        return super(AgregarDocente, self).form_valid(form)
