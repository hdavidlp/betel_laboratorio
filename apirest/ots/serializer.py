from rest_framework import serializers
from .models import OrdenTrabajo, BaseResultados

class OTSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
        
class BaseResultadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseResultados
        fields = '__all__'