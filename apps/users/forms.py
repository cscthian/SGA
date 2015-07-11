# -*- encoding: utf-8 -*-
from django import forms
from .models import User

from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        label='usuario',
        max_length='30',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )
    password = forms.CharField(
        label='contraseña',
        widget=forms.PasswordInput(attrs={'class': 'validate'}),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('usuario o contraseña incorrecta ..!!')
        return self.cleaned_data


class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='contraseña',
        max_length=12,
        widget=forms.PasswordInput(attrs={'class': 'validate'}),
    )
    password2 = forms.CharField(
        label=' repetir contraseña',
        max_length=12,
        widget=forms.PasswordInput(attrs={'class': 'validate'}),
    )

    class Meta:
        model = User
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
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'validate'}),
            'email': forms.EmailInput(attrs={'class': 'validate'}),
            'first_name': forms.TextInput(attrs={'class': 'validate'}),
            'last_name': forms.TextInput(attrs={'class': 'validate'}),
            'phone': forms.TextInput(attrs={'class': 'validate'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'validate'}),
            'address': forms.TextInput(attrs={'class': 'validate'}),
            'gender': forms.Select(attrs={'class': 'validate'}),
            'date_birth': forms.DateInput(attrs={'class': 'datepicker'}),
            'password1': forms.PasswordInput(attrs={'class': 'validate'}),
            'password2': forms.PasswordInput(attrs={'class': 'validate'}),

        }

    def clean_first_name(self):

        name = self.cleaned_data['first_name']
        print '======================'
        print name
        if not name.isalpha():
            self.add_error(
                'first_name',
                'el nombre solo debe contener solo letras..'
            )
        else:
            print 'sali del nombre'
            return name

    def clean_password2(self):
        print '1'
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            print '..........distintas contraseñas............'
            self.add_error('password2', 'las contraseñas no coinciden..!!')
        elif len(password2) < 5:
            print 'menor a 5 caracteres'
            self.add_error(
                'password2',
                'la contraseña debe tener por lo menos 5 caracteres!!'
            )
        else:
            print '***************'
            print 'hola'
            return password2
