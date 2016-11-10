from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from marketing.forms import PromoForm
from .models import Promocion, Producto

# Create your views here.

def acercade(request):
    return render(request, 'marketing/contacto.html')

class CrearPromocion(CreateView):
    form_class = PromoForm
    template_name = 'marketing/promo_form.html'
    success_url = reverse_lazy('')


class ListarHome(ListView):
	template_name='home/index.html'
	model = Producto
	
	def get_context_data(self, **kwargs):
		context = super(ListarHome, self).get_context_data(**kwargs)
		context['promocion'] = Promocion.objects.all()
		return context

	