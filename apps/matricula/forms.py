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
    TURNO_CHOICES = (
        ('m1', '7:00 am - 11:30 am'),
        ('m2', '8:30 am - 1:00 pm'),
        ('t1', '1:00 pm - 5:30 pm'),
        ('n2', '5:30 pm - 10:00 pm'),
    )
    turno = forms.ChoiceField(label='turno', choices=TURNO_CHOICES)

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

class RegistrarMatriculaForm(forms.Form):
    '''clase para registrar una matricula regular'''
    TURNO_CHOICES = (
        ('m1', '7:00 am - 11:30 am'),
        ('m2', '8:30 am - 1:00 pm'),
        ('t1', '1:00 pm - 5:30 pm'),
        ('n2', '5:30 pm - 10:00 pm'),
    )
    alumno = forms.ModelChoiceField(queryset=None, label='Bienvenido : ')
    turno = forms.ChoiceField(label='turno', choices=TURNO_CHOICES)
    modulo = forms.CharField(label='modulo')
    promedio = forms.DecimalField(label='Promedio')
    asignatura = forms.ModelChoiceField(queryset=None, label='Cursos Desaprobados')

    def __init__(self, *args, **kwargs):
        # llamamos al metodo padre mediante el metodo super y sobreescribir
        super(RegistrarMatriculaForm, self).__init__(*args, **kwargs)
        # *args = ??
        # **kwarg son los arqgumentos q se pasan por url
        self.fields['alumno'].queryset = Alumno.objects.filter(user__username = '121314')
        self.fields['asignatura'].queryset = Nota.objects.cursos_cargo()
        #self.fields['promedio'].queryset = Nota.objects.promedio_alumno()
    def clean_promedio(self):
        promedio = self.cleaned_data['promedio']
        if promedio > 20:
            raise forms.ValidationError('Promedio Incorrecto 0<promedio <20')
        return promedio