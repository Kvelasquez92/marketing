from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from marketing.forms import PromoForm

# Create your views here.

class CrearPromocion(CreateView):
    form_class = PromoForm
    template_name = 'marketing/promo_form.html'
    success_url = reverse_lazy('')


def index(request):
	return render(request, 'home/index.html')

	