from django import forms
from .models import *

#creamos el form alumno
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ("__all__") 
        
class PreMatriculaForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ("__all__") 

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ("__all__") 

class DniForm(forms.Form):
    dni = forms.CharField(
        label='ingrese el dni',
        max_length='8',
        widget=forms.TextInput(attrs={'class': 'validate'}),
    )