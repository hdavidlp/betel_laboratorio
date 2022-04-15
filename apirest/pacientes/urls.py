#
from rest_framework import routers
from .views import  PacientesViewsets
from django.urls import path, include

router = routers.DefaultRouter()
router.register('pacientes',PacientesViewsets)


urlpatterns = [
    path('', include(router.urls)),
]
