from django.contrib import admin

# Register your models here.
from .models import Descuento, Estructura_Pago, Aportacion, Detalle_Comprobante, Comprobante

admin.site.register(Descuento)
admin.site.register(Estructura_Pago)
admin.site.register(Aportacion)
admin.site.register(Comprobante)
admin.site.register(Detalle_Comprobante)
