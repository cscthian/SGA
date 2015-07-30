from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from django.core.urlresolvers import reverse_lazy

from .models import User
from .forms import LoginForm, RegistroUserForm
from braces.views import LoginRequiredMixin


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

class AlumnoView(FormView):
    success_url = reverse_lazy('matricula_app:panel_alumno')


class AgregarAdministrador(LoginRequiredMixin, FormView):
    template_name = 'users/administrador/panel/agregar_administrador.html'
    login_url = reverse_lazy('users_app:login')
    form_class = RegistroUserForm
    success_url = reverse_lazy('users_app:panel_admin')

    def form_valid(self, form):
        user = form.save()
        user.type_user = '4'
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super(AgregarAdministrador, self).form_valid(form)

    def form_invalid(self, form):
        print 'form eroors'
        return super(AgregarAdministrador, self).form_invalid(form)

class AgregarCajero(LoginRequiredMixin, FormView):
    template_name = 'users/administrador/panel/agregar-cajero.html'
    login_url = reverse_lazy('users_app:login')
    form_class = RegistroUserForm
    success_url = reverse_lazy('users_app:panel_admin')

    def form_valid(self, form):
        user = form.save()
        user.type_user = '3'
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super(AgregarCajero, self).form_valid(form)

    def form_invalid(self, form):
        print 'form eroors'
        return super(AgregarCajero, self).form_invalid(form)

class AgregarDocente(LoginRequiredMixin, FormView):
    template_name = 'users/administrador/panel/agregar-cajero.html'
    login_url = reverse_lazy('users_app:login')
    form_class = RegistroUserForm
    success_url = reverse_lazy('users_app:panel_admin')

    def form_valid(self, form):
        user = form.save()
        user.type_user = '2'
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super(AgregarDocente, self).form_valid(form)

    def form_invalid(self, form):
        print 'form eroors'
        return super(agregarDocente, self).form_invalid(form)

class DistribuirPanel(View):
    def get(self, request):
        usuario = self.request.user
        if usuario.type_user=='4':
            return render(request, 'users/panel/panel.html')
        else:
            if usuario.type_user == '2':
                return render(request, 'docente/panel.html')
            else:
                if usuario.type_user == '3':
                    return render(request, 'cajero/panel.html')
                else:
                    return render(request, 'alumno/panel.html')

