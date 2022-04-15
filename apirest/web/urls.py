from rest_framework import routers


from .views import AnalisisValidosCargoViewsets, CargoViewsets, ComposicionAnalisisViewsets
from .views import MedicosViewsets,  PruebaViewsets, AnalisisViewsets, RangoViewsets
from django.urls import path, include

router = routers.DefaultRouter()
router.register('prueba', PruebaViewsets)
router.register('analisis', AnalisisViewsets)
router.register('rango', RangoViewsets)
router.register('compoicionAnalisis', ComposicionAnalisisViewsets)
router.register('cargo', CargoViewsets)
router.register('analisisvalidoscargo', AnalisisValidosCargoViewsets)
router.register('medicos', MedicosViewsets)


urlpatterns = [
    path('api/', include(router.urls)),
]
