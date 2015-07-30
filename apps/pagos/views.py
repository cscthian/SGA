from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin, FormView
from django.core.urlresolvers import reverse_lazy

from .forms import DescuentoForm, EstructuraPagosForm, PagoForm, DescuentoForm
from .models import Descuento, Estructura_Pago, Aportacion, Comprobante

from apps.matricula.models import Matricula
from braces.views import LoginRequiredMixin

from django.utils import timezone


class DescuentoView(LoginRequiredMixin, TemplateView):
    template_name = 'mantenimientos/descuento/panel_descuento.html'
    login_url = reverse_lazy('users_app:login')

    def get_context_data(self, **kwargs):
        context = super(DescuentoView, self).get_context_data(**kwargs)
        context['descuentos'] = Descuento.objects.all()
        context['cantidad'] = context['descuentos'].count()
        return context


class DetalleDescuento(LoginRequiredMixin, DetailView):
    template_name = 'mantenimientos/descuento/detalle_descuento.html'
    login_url = reverse_lazy('users_app:login')
    model = Descuento


class AgregarDescuento(LoginRequiredMixin, CreateView):
    form_class = DescuentoForm
    template_name = 'mantenimientos/descuento/agregar_descuento.html'
    login_url = reverse_lazy('users_app:login')
    success_url = reverse_lazy('pagos_app:panel_descuento')


class ModificarDescuento(LoginRequiredMixin, UpdateView):
    model = Descuento
    template_name = 'mantenimientos/descuento/modificar_descuento.html'
    login_url = reverse_lazy('users_app:login')
    success_url = reverse_lazy('pagos_app:panel_descuento')
    form_class = DescuentoForm


class EliminarDescuento(LoginRequiredMixin, DeleteView):
    template_name = 'mantenimientos/descuento/eliminar_descuento.html'
    login_url = reverse_lazy('users_app:login')
    model = Descuento
    success_url = reverse_lazy('pagos_app:panel_descuento')


class EstructurapagoView(LoginRequiredMixin, TemplateView):
    template_name = 'mantenimientos/estructurapagos/panel_estructurapagos.html'
    login_url = reverse_lazy('users_app:login')

    def get_context_data(self, **kwargs):
        context = super(EstructurapagoView, self).get_context_data(**kwargs)
        context['EstructuraPagos'] = Estructura_Pago.objects.all()
        context['cantidad'] = context['EstructuraPagos'].count()
        return context


class DetalleEstructuraPagos(LoginRequiredMixin, DetailView):
    template_name = 'mantenimientos/estructurapagos/detalle_estructurapagos.html'
    login_url = reverse_lazy('users_app:login')
    model = Estructura_Pago


class AgregarEstructuraPagos(LoginRequiredMixin, CreateView):
    form_class = EstructuraPagosForm
    template_name = 'mantenimientos/estructurapagos/agregar_estructurapagos.html'
    login_url = reverse_lazy('users_app:login')
    success_url = reverse_lazy('pagos_app:panel_estructurapagos')


class ModificarEstructuraPagos(LoginRequiredMixin, UpdateView):
    model = Estructura_Pago
    template_name = 'mantenimientos/estructurapagos/modificar_estructurapagos.html'
    login_url = reverse_lazy('users_app:login')
    success_url = reverse_lazy('pagos_app:panel_estructurapagos')
    form_class = EstructuraPagosForm


class EliminarEstructuraPagos(LoginRequiredMixin, DeleteView):
    template_name = 'mantenimientos/estructurapagos/eliminar_estructurapagos.html'
    login_url = reverse_lazy('users_app:login')
    model = Estructura_Pago
    success_url = reverse_lazy('pagos_app:panel_estructurapagos')


class PanelCajaView(LoginRequiredMixin, TemplateView):
    template_name = 'panel_caja/panel.html'
    login_url = reverse_lazy('users_app:login')


class MatriculaPendiente(LoginRequiredMixin, ListView):

    template_name = 'procesos/pagos/matricula/lista_matricula.html'
    login_url = reverse_lazy('users_app:login')
    paginate_by = 20

    def get_queryset(self):
        # se crea la variable objeto
        self.matriculados = Matricula.objects.matricula_pendiente()
        return self.matriculados

    def get_context_data(self, **kwargs):
        # Llama primero a la implementacion para traer el contexto
        context = super(MatriculaPendiente, self).get_context_data(**kwargs)
        context['cantidad'] = self.matriculados.count()
        return context


class RegistrarPago(LoginRequiredMixin, FormView):
    form_class = PagoForm
    template_name = 'procesos/pagos/matricula/pago_matricula.html'
    login_url = reverse_lazy('users_app:login')
    success_url = reverse_lazy('pagos_app:panel_descuento')

    def get_form_kwargs(self):
        kwargs = super(RegistrarPago, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs.get('pk', 0),
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(RegistrarPago, self).get_context_data(**kwargs)
        matricula_pk = self.kwargs.get('pk', 0)
        # self.get_form() es form_class enviamos el formulario {{ form }}
        context['form'] = self.get_form()
        matricula = Matricula.objects.get(pk=matricula_pk)
        context['matricula'] = matricula
        return context

    def form_valid(self, form):
        
        matricula_pk = self.kwargs.get('pk', 0)
        #datos para la tabla aportacion
        matricula = Matricula.objects.get(pk=matricula_pk)
        concepto = '1'
        monto = form.cleaned_data['monto']        
        fecha = timezone.now()

        aportacion = Aportacion(
            concepto=concepto,
            monto=monto,
            fecha_pago=fecha,
            matricula=matricula
        )
        aportacion.save()
        #datos que se actualizaran en matricula
        matricula.estado_matricula = True
        matricula.saldo = matricula.saldo - monto
        if matricula.saldo == 0:
            matricula.completado = True
        #actualizamos la tabla matricula
        matricula.save()
        #datos para la tabla comprombante
        tipo = form.cleaned_data['tipo']
        serie = form.cleaned_data['serie']
        numero = form.cleaned_data['numero']
        descuento =form.cleaned_data['descuento']
        #convertimos el descuento en su porcntaje
        monto_descuento = monto*(descuento.porcentaje/100)
        sub_total = monto - monto_descuento

        comprabante = Comprobante(
            tipo=tipo,
            serie=serie,
            numero=numero,
            monto_subtotal = monto,
            monto_igv=0,
            monto_total=sub_total,
        )
        comprabante.save()
        #proceso de inicializacion de notas
        notas = matricula.modulo.asignatura
        return super(RegistrarPago, self).form_valid(form)

class DescuentoMatriculaView(LoginRequiredMixin, FormMixin, DetailView):
    model = Matricula
    form_class = DescuentoForm
    template_name = 'procesos/pagos/matricula/descuento_alumno.html'
    login_url = reverse_lazy('users_app:login')


    def get_success_url(self):
        return reverse_lazy('pagos_app:pago_matricula',kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(DescuentoMatriculaView, self).get_context_data(**kwargs)
        # self.get_form() es form_class enviamos el formulario {{ form }}
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        # get_object() es el parametro matricula q se psa por url
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        descuento = form.cleaned_data['descuento']
        matricula = self.object
        saldo_actual = matricula.saldo
        porcentaje = descuento.porcentaje
        nuevo_saldo = saldo_actual-(saldo_actual*porcentaje/100)
        matricula.saldo = nuevo_saldo
        matricula.save()
        print porcentaje
        print descuento
        print nuevo_saldo
        return super (DescuentoMatriculaView,self).form_valid(form)