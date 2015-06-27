from django import forms
from .models import *

#creamos el form alumno
class AlumnoForm(forms.ModelForm):
	class Meta:
		model = Alumno
		fields = ("__all__") 


#creamos el form Carrera
class CarreraForm(forms.ModelForm):
	class Meta:
		model = Carrera
		fields = ("__all__") 


#creamos el form Modulo
class ModuloForm(forms.ModelForm):
	class Meta:
		model = Modulo
		fields = ("__all__") 


#creamos el form Asignatura
class AsignaturaForm(forms.ModelForm):
	class Meta:
		model = Asignatura
		fields = ("__all__") 

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ("__all__") 

#creamos el form matricula
class MatriculaForm(forms.ModelForm):
	class Meta:
		model = Matricula
		fields = ("__all__")


#creamos el form notas
class NotaForm(forms.ModelForm):
	class Meta:
		model = Nota
		fields = ("__all__") 


#creamos form de matricula detalle
class MatriculaDetalleForm(forms.ModelForm):
	class Meta:
		model = MatriculaDetalle
		fields = ("__all__") 


class DniForm(forms.Form):
	dni = forms.CharField(max_length=8)