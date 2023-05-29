from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    cuit=models.IntegerField(max_length=11, unique=True)
    def __str__(self) -> str:
        return f"{self.nombre} {self.cuit}"

class Productos(models.Model):
    producto=models.CharField(max_length=50, unique=True)
    descripcion=models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.producto}: {self.descripcion}"

class Vendedores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"