from rest_framework import routers
# from .views import  PacientesViewsets
from .views import OTViewsets, BaseResultadosViewsets
from django.urls import path, include

router = routers.DefaultRouter()
router.register('ordenes',OTViewsets)
router.register('baseresultados', BaseResultadosViewsets)


urlpatterns = [
    path('', include(router.urls)),
]
