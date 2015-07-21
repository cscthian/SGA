# -*- encoding: utf-8 -*-
from django import forms
from .models import *

from apps.users.forms import UserForm
from apps.notas.models import *
#creamos el form alumno


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ("__all__")


class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ("__all__")

class ProgramacionForm(forms.ModelForm):
    class Meta:
        model = Programacion
        fields = ("__all__")
        widgets = {
            'inicio': forms.DateInput(attrs={'class': 'datepicker'}),
            'fin': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class DniForm(forms.Form):
    dni = forms.CharField(
        label='ingrese el dni',
        max_length='8',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )


class PreMatriculaForm(UserForm):
    '''clase para registra pre-matricula'''

    carrera_profesional = forms.ModelChoiceField(queryset=None)
    turno = forms.ModelChoiceField(label='turno', queryset=None)
    class Meta(UserForm.Meta):
        # campos q se van a mostar en el formulario pre_matricula
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'avatar',
            'address',
            'phone',
            'gender',
            'date_birth',
        )

    def __init__(self, *args, **kwargs):
        # llamamos al metodo padre mediante el metodo super y sobreescribir
        super(PreMatriculaForm, self).__init__(*args, **kwargs)
        # *args = ??
        # **kwarg son los arqgumentos q se pasan por url
        self.fields['carrera_profesional'].queryset = Carrera.objects.all()
        self.fields['turno'].queryset = Turno.objects.all()

class RegistrarMatriculaForm(forms.Form):
    '''clase para registrar una matricula regular'''
    #alumno = forms.ModelChoiceField(queryset=None, label='Bienvenido : ')
    turno = forms.ModelChoiceField(label='turno', queryset=None)
    #modulo = forms.CharField(label='modulo')
    #promedio = forms.ModelChoiceField(label='Promedio')
    asignatura = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=None,
        required=False,
        )

    def __init__(self,user,*args, **kwargs):
        # llamamos al metodo padre mediante el metodo super y sobreescribir
        super(RegistrarMatriculaForm, self).__init__(*args, **kwargs)
        # **kwarg son los arqgumentos q se pasan por url
        #self.fields['alumno'].queryset = Alumno.objects.filter(user__username=user)
        self.fields['asignatura'].queryset = Nota.objects.cursos_cargo(user)
        self.fields['turno'].queryset = Turno.objects.all()
        #self.fields['promedio'].queryset = Nota.objects.promedio_alumno()
    # def clean_promedio(self):
    #     promedio = self.cleaned_data['promedio']
    #     if promedio > 20:
    #         raise forms.ValidationError('Promedio Incorrecto 0<promedio <20')
    #     return promedio