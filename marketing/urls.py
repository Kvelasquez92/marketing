from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from marketing.views import CrearPromocion, acercade, ListarHome, ViewMenu, ViewPromo



urlpatterns = [
    url(r'^$', acercade, name = 'acerca_de'),
    url(r'^nueva_promo$', CrearPromocion.as_view(), name='crear_promocion'),
    url(r'^home/',ListarHome.as_view(), name='index'),
    url(r'^menu/',ViewMenu.as_view(), name='menu'),
    url(r'^promocion/',ViewPromo.as_view(), name='promo'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
