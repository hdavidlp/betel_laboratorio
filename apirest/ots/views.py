from django.shortcuts import render
from rest_framework import viewsets
from .models import OrdenTrabajo, BaseResultados
from .serializer import OTSerializer, BaseResultadosSerializer


# Create your views here.
class OTViewsets(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class =  OTSerializer
    
    
class BaseResultadosViewsets(viewsets.ModelViewSet):
    queryset =  BaseResultados.objects.all()
    serializer_class =  BaseResultadosSerializer