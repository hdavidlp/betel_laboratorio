from rest_framework import routers


from .views import AnalisisValidosCargoViewsets, CargoViewsets, ComposicionAnalisisViewsets
from .views import MedicosViewsets, PacientesViewsets, PruebaViewsets, AnalisisViewsets, RangoViewsets, OTViewsets, BaseResultadosViewsets
from django.urls import path, include

router = routers.DefaultRouter()
router.register('prueba', PruebaViewsets)
router.register('analisis', AnalisisViewsets)
router.register('rango', RangoViewsets)
router.register('compoicionAnalisis', ComposicionAnalisisViewsets)
router.register('cargo', CargoViewsets)
router.register('analisisvalidoscargo', AnalisisValidosCargoViewsets)
router.register('pacientes', PacientesViewsets )
router.register('medicos', MedicosViewsets)
router.register('ot', OTViewsets)
router.register('baseresultados', BaseResultadosViewsets)

urlpatterns = [
    path('api/', include(router.urls)),
]
