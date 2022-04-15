from django.db import models
from web.models import Medico, Cargo
from pacientes.models import Paciente

# Create your models here.
class OrdenTrabajo(models.Model):
    fecha = models.DateField()
    secuencia = models.SmallIntegerField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    
    
class BaseResultados(models.Model):
    ot = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)
    idAnalisis = models.IntegerField()
    nombre_Anlisis = models.CharField(max_length=120)
    prueba = models.CharField(max_length=50)
    resultado = models.TextField(null=True, blank=True )
    udm = models.CharField(max_length=20, blank=True, null=True)
    minimo = models.CharField(max_length=10, null=True, blank=True)
    maximo = models.CharField(max_length=10, null=True, blank=True)
    tipo = models.CharField(max_length=10)
    fuera_rango = models.CharField(max_length=20)
    nota_Encabezado_Analisis = models.TextField(null=True, blank=True)
    nota_Pie_Analisis = models.TextField(null=True, blank=True)
    agrupador1 = models.TextField(null=True, blank=True)
    nota_Encabezado_Agrupador1 = models.TextField(null=True, blank=True)
    nota_Pie_Agrupador1 = models.TextField(null=True, blank=True)
    agrupador2 = models.TextField(null=True, blank=True)
    nota_Encabezado_Agrupador2 = models.TextField(null=True, blank=True)
    nota_Pie_Agrupador2 = models.TextField(null=True, blank=True)
    nota_Prueba = models.TextField(null=True, blank=True)