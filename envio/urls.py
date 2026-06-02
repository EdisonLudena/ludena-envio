from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RutaViewSet, PaqueteViewSet
from .services_views import costos_view

router = DefaultRouter()
router.register(r"rutas", RutaViewSet,  basename="rutas")
router.register(r"paquetes", PaqueteViewSet, basename="paquetes")

urlpatterns = [path('envio/cobros/', costos_view, name='cobros')]
urlpatterns += router.urls