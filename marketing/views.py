from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
import datetime
import os
from django.conf import settings
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy

from marketing.forms import PromoForm, CorreoForm, RecetaForm
from .models import Promocion, Receta, Suscriptores

# Create your views here.

meses = [
    ' ', 'Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre', 'Diciembre',
]

class CrearPromocion(CreateView):
    form_class = PromoForm
    template_name = 'marketing/promo_form.html'
    success_url = reverse_lazy('promocion:promo')

class RegistrarCorreo(CreateView):
    form_class = CorreoForm
    template_name = 'marketing/contacto.html'
    success_url = reverse_lazy('promocion:acerca_de')

def EnviarCorreo(request):
    asunto = 'Nuevas promociones BLISS'
    promociones = Promocion.objects.all()[:2]
    automensaje = 'visita nuestros restaurantes este mes de ' + meses[datetime.datetime.now().month] + ' y prueba nuestras promociones: \n\n'
    for promo in promociones:
        automensaje = automensaje + promo.nombre + ':\n' + promo.descripcion + '\n' + 'a un precio super especial de:\nQ'+ str(promo.precio) +'\n\n'
    suscriptors = Suscriptores.objects.all()
    for suscriptor in suscriptors:
        mensaje = 'Hola ' + suscriptor.nombre + '!\n' + automensaje
        mail = EmailMessage(asunto, mensaje, to = [suscriptor.correo])
        mail.attach_file(os.path.join(settings.MEDIA_ROOT, promociones[0].imagen.path))
        mail.attach_file(os.path.join(settings.MEDIA_ROOT, promociones[1].imagen.path))
        mail.send()
        mensaje = automensaje
    return redirect('promocion:index')
    return render(request,'home/index.html')

class ListarHome(ListView):
	template_name='home/index.html'
	model = Receta

	def get_context_data(self, **kwargs):
		context = super(ListarHome, self).get_context_data(**kwargs)
		context['promocion'] = Promocion.objects.all()[:3]
		return context

class ListarRecetaImagen(ListView):
    template_name='marketing/imagenes_recetas.html'
    model = Receta
    paginate_by = 3

class ViewMenu(ListView):
	template_name='marketing/menu.html'
	model = Receta

class EditarImagenReceta(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'marketing/receta_form.html'
    success_url = reverse_lazy('promocion:receta_listar')

class ViewPromo(ListView):
	template_name='marketing/promocion.html'
	model = Promocion

class DetallePromocion(DetailView):
    template_name = 'marketing/detalle_promo.html'
    model = Promocion

    def get_context_data(self, **kwargs):
        context = super(DetallePromocion, self).get_context_data(**kwargs)
        context['real'] = context['object'].precio - context['object'].descuento
        context['promocion'] = Promocion.objects.exclude(id = context['object'].id)[:3]
        return context

class DetalleProducto(DetailView):
    model = Receta
    template_name = 'marketing/detalle_producto.html'

    def get_context_data(self, **kwargs):
        context = super(DetalleProducto, self).get_context_data(**kwargs)
        context['productos'] = Receta.objects.exclude(id = context['object'].id)[:3]
        return context
