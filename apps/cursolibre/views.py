from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import FormView, FormMixin

from apps.users.forms import UserForm
from apps.users.models import User

from .models import AsignaturaLibre, Ciclo, MatriculaCursoLibre
from .forms import *

from datetime import datetime

from django.core.urlresolvers import reverse_lazy
# Create your views here.


class MatriculaCurso(FormView):
    model = AsignaturaLibre
    form_class = DniForm
    template_name = 'matricula_cursolibre.html'

    def get_success_url(self):
        return reverse_lazy('matricula_app:mensaje_confirmacion')

    def get_context_data(self, **kwargs):
            context = super(MatriculaCurso, self).get_context_data(**kwargs)
            context['form'] = self.get_form()
            return context     

    def form_valid(self, form):
        username = form.cleaned_data['username']
        usuario = User.objects.get(username=username)
        asignatura_pk = self.kwargs.get('pk', 0)
        #recuperamos la palara clave de url
        asignatura = AsignaturaLibre.objects.get(pk=asignatura_pk)
        saldo = asignatura.costo
        print saldo
        fecha = datetime.now()
        print '======= 1 ======='

        ciclo = Ciclo.objects.all()[0]
        print '======= 2 ======='

        matricula = MatriculaCursoLibre(
            alumno=usuario,
            asignatura=asignatura,
            fecha=fecha,
            saldo=saldo,
            ciclo=ciclo,
        )
        matricula.save()


        print matricula

        return super(MatriculaCurso, self).form_valid(form)


class PreMatriculaCurso(FormView):
    form_class = UserForm
    template_name = 'matricula_cursolibre.html'
    success_url = reverse_lazy('matricula_app:mensaje_confirmacion')

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

# class RegistrarPagoCursoLibre(LoginRequiredMixin, FormView):
#     form_class = PagoLibreForm
#     template_name = 'modificar_libre.html'
#     login_url = reverse_lazy('users_app:login')
#     success_url = reverse_lazy('matricula_app:mensaje_confirmacion')

#     def get_form_kwargs(self):
#         kwargs = super(RegistrarPagoCursoLibre, self).get_form_kwargs()
#         kwargs.update({
#             'pk': self.kwargs.get('pk', 0),
#         })
#         return kwargs

#     def get_context_data(self, **kwargs):
#         context = super(RegistrarPagoCursoLibre, self).get_context_data(**kwargs)
#         matricula_pk = self.kwargs.get('pk', 0)
#         # self.get_form() es form_class enviamos el formulario {{ form }}
#         context['form'] = self.get_form()
#         matricula = Matricula.objects.get(pk=matricula_pk)
#         context['matricula'] = matricula
#         return context

#     def form_valid(self, form):
        
#         matricula_pk = self.kwargs.get('pk', 0)
#         #datos para la tabla aportacion
#         matricula = MatriculaCursoLibre.objects.get(pk=matricula_pk)
#         estado = form.cleaned_data['estado']        
#         #datos que se actualizaran en matricula
#         matricula.estado_matricula = True
#         matricula.saldo = 0
#         #actualizamos la tabla matricula
#         #matricula.save()
#         #proceso de inicializacion de notas
#         return super(RegistrarPagoCursoLibre, self).form_valid(form)