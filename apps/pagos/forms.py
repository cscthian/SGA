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


class PagoForm(forms.ModelForm):
    monto = forms.DecimalField(max_digits=10, decimal_places=5, required=True)
    descuento = forms.ModelChoiceField(queryset=None)

    class Meta:
        model = Comprobante
        fields = ('tipo', 'serie', 'numero')

    def __init__(self, *args, **kwargs):
        # llamamos al metodo padre mediante el metodo super y sobreescribir
        super(PagoForm, self).__init__(*args, **kwargs)
        # *args = ??
        # **kwarg son los arqgumentos q se pasan por url
        self.fields['descuento'].queryset = Descuento.objects.all()
