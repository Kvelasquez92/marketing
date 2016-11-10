from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from marketing.views import CrearPromocion, acercade, ListarHome



urlpatterns = [
    url(r'^/', acercade, name = 'acerca_de'),
    url(r'^nueva_promo$', CrearPromocion.as_view(), name='crear_promocion'),
    url(r'^home/',ListarHome.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
