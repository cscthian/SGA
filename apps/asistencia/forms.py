# -*- encoding: utf-8 -*-
from django import forms


class DniForm(forms.Form):
    dni = forms.CharField(
        label='ingrese el dni',
        max_length='8',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )

    # def clean(self):
    #     cleaned_data = super(LoginForm, self).clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')

    #     if not authenticate(username=username, password=password):
    #         raise forms.ValidationError('usuario o contraseña incorrecta ..!!')
    #     return self.cleaned_data
