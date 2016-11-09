from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from marketing.views import CrearPromocion

urlpatterns = [
    url(r'^nueva_promo$', CrearPromocion.as_view(), name='crear_promocion'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
