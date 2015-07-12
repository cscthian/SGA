from django import forms 
from models import Descuento, Estructura_Pago, Comprobante

#creamos formulario descuento
class DescuentoForm(forms.ModelForm):
    class Meta:
    	model = Descuento
    	fields = ("__all__")
    	

class EstructuraPagosForm(forms.ModelForm):
    class Meta:
    	model = Estructura_Pago
    	fields = ("__all__")

    	widgets = {
    	'fecha_limite1': forms.DateInput(attrs={'class': 'datepicker'}), 
    	'fecha_limite2': forms.DateInput(attrs={'class': 'datepicker'}), 
    	'fecha_limite3': forms.DateInput(attrs={'class': 'datepicker'}), 
    	'fecha_limite4': forms.DateInput(attrs={'class': 'datepicker'}), 
    	}

class ComprobanteForm(forms.ModelForm):
	class Meta:
		model = Comprobante
		fields = ("__all__")
