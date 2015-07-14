from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class PanelDocenteView(TemplateView):
    template_name = 'panel_docente/panel.html'
