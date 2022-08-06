from django.db import models

# Create your models here.
class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField()

class Actividad(models.Model):

    nombre_actividad = models.CharField(max_length=50)

