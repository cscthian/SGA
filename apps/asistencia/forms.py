# -*- encoding: utf-8 -*-
from django import forms
from .models import Horario, Aula

from apps.users.forms import RegistroUserForm


class DniForm(forms.Form):
    dni = forms.CharField(
        label='ingrese su dni',
        max_length='8',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if not dni.digit():
            msj = 'no dni no peude contener caracteres'
            self.add_error('dni', msj)
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
        ('1', 'administracion de bases de datos'),
        ('2', 'analista de sistemas'),
        ('3', 'administracion de centros de computo'),
        ('4', 'cursos generales'),
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
