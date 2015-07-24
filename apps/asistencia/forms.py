# -*- encoding: utf-8 -*-
from django import forms
from django.forms.models import ModelMultipleChoiceField

from .models import Horario, Aula, Docente, CargaAcademica

from apps.matricula.models import Matricula

from apps.users.forms import RegistroUserForm

from datetime import datetime


class DniForm(forms.Form):
    dni = forms.CharField(
        label='ingrese su dni',
        max_length='8',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if not dni.isdigit():
            msj = 'el dni no peude contener caracteres'
            self.add_error('dni', msj)
        elif len(dni) != 8:
            msj = 'el numero de digitos debe ser 8'
            self.add_error('dni', msj)
        elif not Docente.objects.es_docente(dni):
            msj = 'usted no es un docente'
            self.add_error('dni', msj)
        elif not CargaAcademica.objects.tiene_carga(dni):
            msj = 'usted no tiene clases el dia de hoy'
            self.add_error('dni', msj)
        else:
            return dni
    # def clean(self):
    #     cleaned_data = super(LoginForm, self).clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ('__all__')


class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ('__all__')


class DocenteForm(RegistroUserForm):
    TIPO_CHOICES = (
        ('contratado', 'contratado'),
        ('nombrado', 'nombrado'),
    )
    ESPECIALIDAD_CHOICES = (
        ('1', 'administrador'),
        ('2', 'economista'),
        ('3', 'ingeniero'),
        ('4', 'matematico'),
        ('5', 'contador'),
        ('6', 'analista de sistemas'),
    )
    tipo_docente = forms.ChoiceField(
        label='tipo de docente',
        choices=TIPO_CHOICES,
        required=True,
    )
    especialidad = forms.ChoiceField(
        label='especialidad',
        choices=ESPECIALIDAD_CHOICES,
        required=True,
    )
    titulo = forms.CharField(required=True, max_length=20)

    class Meta(RegistroUserForm.Meta):
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
            'tipo_docente',
            'especialidad',
            'titulo',
            'password1',
            'password2',
        )


class GrupoForm(forms.Form):
    turno = forms.ModelChoiceField(
        queryset=None,
        required=True,
    )

    def __init__(self, user, *args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)


class AsistenciaAlumnoForm(forms.Form):
    alumnos = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=None,
        required=False,
    )

    def __init__(self, pk, user, grupo, *args, **kwargs):
        super(AsistenciaAlumnoForm, self).__init__(*args, **kwargs)
        hoy = datetime.now()
        asignatura = pk
        docente = user

        alumnos = Matricula.objects.filter(
            modulo__asignatura=asignatura,
            turno=grupo,
            programacion__inicio__lte=hoy,
            programacion__fin__gte=hoy,
        )

        self.fields['alumnos'].queryset = alumnos
