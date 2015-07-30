from django import forms
from .models import Asignatura, Modulo, Nota


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ('__all__')


class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ('__all__')

class NotaForm(forms.ModelForm):
	class Meta:
		model = Nota
		fields = ('asignatura','nota1','nota2','nota3','nota4','promedio')
