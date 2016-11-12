from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy

from marketing.forms import PromoForm, CorreoForm, RecetaForm
from .models import Promocion, Receta, Suscriptores

# Create your views here.

class CrearPromocion(CreateView):
    form_class = PromoForm
    template_name = 'marketing/promo_form.html'
    success_url = reverse_lazy('')

class RegistrarCorreo(CreateView):
    form_class = CorreoForm
    template_name = 'marketing/contacto.html'
    success_url = reverse_lazy('promocion:index')

def EnviarCorreo(request):
    if request.method == 'POST':
        asunto = 'Menseaje de prueba'
        mensaje = 'Cuerpo del correo de prueba'
        for suscriptor in Suscriptores.objects.all():
            mail = EmailMessage(asunto, mensaje, to = [suscriptor.correo])
            mail.send()
        return HttpResponseRedirect('/home')
    return render_to_response('home/index.html', context_instance=RequestContext(request))

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
	template_name='marketing/menu.html'
	model = Promocion
