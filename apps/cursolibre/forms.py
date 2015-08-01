from django import forms
from models import *


class DniForm(forms.Form):
    username = forms.CharField(
        label='dni',
        max_length='8',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )