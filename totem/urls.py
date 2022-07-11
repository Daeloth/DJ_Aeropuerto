from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="totem/index"),
    path("ingreso/", views.ingreso, name="totem/ingreso"),
    path("registro/", views.registro, name="totem/registro"),
    path("transfer/", views.transfer, name="totem/transfer"),
    path("pago/", views.pago, name="totem/pago"),
    path("pagof/", views.pagof, name="totem/pagof"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
