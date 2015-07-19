from django import forms
from .models import Asignatura, Modulo


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ('__all__')


class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ('__all__')
