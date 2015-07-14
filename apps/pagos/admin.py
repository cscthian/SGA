from django.contrib import admin

# Register your models here.
from .models import Descuento, Estructura_Pago

admin.site.register(Descuento)
admin.site.register(Estructura_Pago)

