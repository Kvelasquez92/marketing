from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required as lr

from marketing.views import CrearPromocion, ListarHome, ViewMenu, ViewPromo, EnviarCorreo, \
							RegistrarCorreo, ListarRecetaImagen, EditarImagenReceta, \
							DetallePromocion, DetalleProducto


urlpatterns = [
    url(r'^sobre_nosotros/', RegistrarCorreo.as_view(), name = 'acerca_de'),
    url(r'^recetas/', lr(ListarRecetaImagen.as_view()), name='receta_listar'),
    url(r'^receta/editar/(?P<pk>\d+)$', lr(EditarImagenReceta.as_view()), name='receta_editar'),
    url(r'^nueva_promo', lr(CrearPromocion.as_view()), name='crear_promocion'),
    url(r'^home/',ListarHome.as_view(), name='index'),
    url(r'^menu/',ViewMenu.as_view(), name='menu'),
    url(r'^promocion/',ViewPromo.as_view(), name='promo'),
    url(r'^sendmail/',EnviarCorreo, name='mailing'),
    url(r'^detalle/(?P<pk>\d+)/$', DetallePromocion.as_view(), name='detalle_promocion'),
    url(r'^detalle/receta/(?P<pk>\d+)/$', DetalleProducto.as_view(), name='detalle_producto'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
