from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .forms import DniForm
from .models import Aula


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
