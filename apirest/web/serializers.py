from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Analisis, BaseResultados, Cargo, ComposicionAnalisis, Medico, OrdenTrabajo,  Prueba, Rango, AnalisisValidosCargo



class PruebaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Prueba
        fields='__all__'
        
class AnalisisSerializers(serializers.ModelSerializer):
    class Meta:
        model=Analisis
        fields='__all__'
        
class RangoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rango
        fields='__all__'
        
class ComposicionAnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model=ComposicionAnalisis
        fields='__all__'
        
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'
        
class AnalisisValidosCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalisisValidosCargo
        fields = '__all__'

# class PacientesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Paciente
#         fields = '__all__'
        
class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class OTSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
        
class BaseResultadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseResultados
        fields = '__all__'
        

        
        
        