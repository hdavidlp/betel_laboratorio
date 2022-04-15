from django.db import models
from datetime import date

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=2)
    notas = models.TextField(null=True, blank=True)
    
    
    def edad(self):
        days_in_year = 365.2425    
        age = int((date.today() - self.fechaNacimiento).days / days_in_year) 
        return age 
    
    def __str__(self):
        return str(self.id) + ", " + self.nombre + ", " + self.apellidos
