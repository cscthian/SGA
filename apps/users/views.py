from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from django.core.urlresolvers import reverse_lazy

from .models import User
from .forms import LoginForm, RegistroUserForm


class LogIn(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '/'

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            if user.is_active:
                login(self.request, user)
        return super(LogIn, self).form_valid(form)


def LogOut(request):
    logout(request)
    return redirect('/')


class AdminView(TemplateView):
    template_name = 'users/panel/panel.html'


class DocenteView(TemplateView):
    template_name = 'users/docente/panel/docente_panel.html'


class AgregarAdministrador(FormView):
    template_name = 'users/administrador/panel/agregar_administrador.html'
    form_class = RegistroUserForm
    success_url = reverse_lazy('asistencia_app:panel_aula')

    def form_valid(self, form):
        user = form.save()
        user.type_user = '4'
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super(AgregarAdministrador, self).form_valid(form)

    def form_invalid(self, form):
        print 'form eroors'
        return super(AgregarAdministrador, self).form_invalid(form)
