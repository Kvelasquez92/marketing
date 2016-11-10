from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from marketing.views import CrearPromocion, index 

urlpatterns = [
    url(r'^nueva_promo$', CrearPromocion.as_view(), name='crear_promocion'),
    url(r'^',index, name='index'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
