from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from marketing.forms import PromoForm

# Create your views here.

def acercade(request):
    return render(request, 'marketing/contacto.html')

class CrearPromocion(CreateView):
    form_class = PromoForm
    template_name = 'marketing/promo_form.html'
    success_url = reverse_lazy('')
