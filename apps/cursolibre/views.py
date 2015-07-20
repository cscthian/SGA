from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView, FormMixin

from apps.users.forms import UserForm
from apps.users.models import User

from .models import AsignaturaLibre, Ciclo, MatriculaCursoLibre
from .forms import DniForm

from datetime import datetime

from django.core.urlresolvers import reverse_lazy
# Create your views here.


class MatriculaCurso(FormMixin, DetailView):
    model = AsignaturaLibre
    form_class = DniForm
    template_name = 'matricula_cursolibre.html'

    def get_success_url(self):
        return reverse_lazy('matricula_app:inicio')

    def get_context_data(self, **kwargs):
            context = super(MatriculaCurso, self).get_context_data(**kwargs)
            context['form'] = self.get_form()
            return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        asignatura = self.object
        saldo = asignatura.costo
        fecha = datetime.now()

        ciclo = Ciclo.objects.all()[0]

        matricula = MatriculaCursoLibre(
            alumno=username,
            asignatura=asignatura,
            fecha=fecha,
            saldo=asignatura.costo,
            ciclo=ciclo,
        )
        matricula.save()


        print username
        print fecha

        return super(MatriculaCurso, self).form_valid(form)


class PreMatriculaCurso(FormView):
    form_class = UserForm
    template_name = 'matricula_cursolibre.html'
    success_url = reverse_lazy('matricula_app:inicio')

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
        tipo_user = '5'
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
        return super(PreMatriculaCurso, self).form_valid(form)
