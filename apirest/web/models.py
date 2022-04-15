from ast import Delete
from email.policy import default
from mailbox import NoSuchMailboxError
from tkinter import CASCADE
from unittest import signals
from django.db import models
from datetime import date

from pacientes.models import Paciente 


class Analisis(models.Model):
    nombre = models.CharField(max_length=120)
    nombre_corto = models.CharField(max_length=80,blank=True, null=True)
    nota_Encabezado = models.TextField(blank=True, null=True)
    nota_Pie = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.id) + ", " + self.nombre_corto


class Prueba(models.Model):
    nombre = models.CharField(max_length=50)
    udm = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=10)
    siglas = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.id) + ", " + self.nombre
    
class ComposicionAnalisis(models.Model):
    analisis = models.ForeignKey(Analisis, on_delete=models.CASCADE)
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    secuencia = models.SmallIntegerField()
       
    
class Rango(models.Model):
    minimo = models.CharField(max_length=10, null=True, blank=True)
    maximo = models.CharField(max_length=10, null=True, blank=True)
    edad_minima = models.DecimalField(max_digits=5, decimal_places=2)    
    edad_maxima = models.DecimalField(max_digits=5, decimal_places=2)    
    sexo = models.CharField(max_length=2)
    detalle = models.CharField(max_length=30)
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    
class Cargo(models.Model):
    descripcion = models.CharField(max_length=80)
    notas = models.TextField()
    default = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id) + ", " + self.descripcion
    
class AnalisisValidosCargo(models.Model):
    costo = models.DecimalField(max_digits=9, decimal_places=2)
    nota = models.CharField(max_length=40, null=True, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    analisis = models.ForeignKey(Analisis, on_delete=models.CASCADE)

# class Paciente(models.Model):
#     nombre = models.CharField(max_length=25)
#     apellidos = models.CharField(max_length=25)
#     fechaNacimiento = models.DateField()
#     sexo = models.CharField(max_length=2)
#     notas = models.TextField(null=True, blank=True)
    
    
#     def edad(self):
#         days_in_year = 365.2425    
#         age = int((date.today() - self.fechaNacimiento).days / days_in_year) 
#         return age 
    
#     def __str__(self):
#         return str(self.id) + ", " + self.nombre + ", " + self.apellidos
        
class Medico(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos= models.CharField(max_length=25)
    notas = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id) + ", " + self.apellidos + " " + self.nombre


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
    
    
    
    
    
    
    