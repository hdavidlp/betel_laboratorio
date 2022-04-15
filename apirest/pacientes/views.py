from django.shortcuts import render
from rest_framework import viewsets
from .models import Paciente
from .serializers import PacientesSerializer

# Create your views here.
class PacientesViewsets(viewsets.ModelViewSet):
    queryset =  Paciente.objects.all()
    serializer_class =  PacientesSerializer
