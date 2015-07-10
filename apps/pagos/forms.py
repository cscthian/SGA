from django import forms 
from models import Descuento

#creamos formulario descuento
class DescuentoForm(forms.ModelForm):
    class Meta:
    	model = Descuento
    	fields = ("__all__")
    	