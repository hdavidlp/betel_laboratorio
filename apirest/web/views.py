from django.shortcuts import render
from rest_framework import viewsets
from .models import Analisis, AnalisisValidosCargo,  Cargo, ComposicionAnalisis, Medico,   Prueba, Rango
from .serializers import PruebaSerializers, AnalisisSerializers, RangoSerializer, ComposicionAnalisisSerializer, CargoSerializer
from .serializers import AnalisisValidosCargoSerializer,  MedicosSerializer

# from ots.models import BaseResultados

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.view

class PruebaViewsets(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializers

@api_view(['POST'])  
def addPrueba(request):
    serializer = PruebaSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
    
class AnalisisViewsets(viewsets.ModelViewSet):
    queryset = Analisis.objects.all()
    serializer_class =  AnalisisSerializers
    
class RangoViewsets(viewsets.ModelViewSet):
    queryset = Rango.objects.all()
    serializer_class =  RangoSerializer
    
class ComposicionAnalisisViewsets (viewsets.ModelViewSet):
    queryset = ComposicionAnalisis.objects.all()
    serializer_class =  ComposicionAnalisisSerializer
    
class CargoViewsets(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class =  CargoSerializer
    
    
class AnalisisValidosCargoViewsets(viewsets.ModelViewSet):
    queryset = AnalisisValidosCargo.objects.all()
    serializer_class =  AnalisisValidosCargoSerializer
    
# class PacientesViewsets(viewsets.ModelViewSet):
#     queryset =  Paciente.objects.all()
#     serializer_class =  PacientesSerializer
    
class MedicosViewsets(viewsets.ModelViewSet):
    queryset =  Medico.objects.all()
    serializer_class =  MedicosSerializer

# class OTViewsets(viewsets.ModelViewSet):
#     queryset = OrdenTrabajo.objects.all()
#     serializer_class =  OTSerializer
    
# class BaseResultadosViewsets(viewsets.ModelViewSet):
#     queryset =  BaseResultados.objects.all()
#     serializer_class =  BaseResultadosSerializer