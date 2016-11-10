from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from marketing.views import CrearPromocion, acercade

urlpatterns = [
    url(r'^', acercade, name = 'acerca_de'),
    url(r'^nueva_promo$', CrearPromocion.as_view(), name='crear_promocion'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
