from django import forms


class DniForm(forms.Form):
    username = forms.CharField(
        label='dni',
        max_length='8',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )
