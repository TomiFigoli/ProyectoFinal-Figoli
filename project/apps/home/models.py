from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    cuit=models.IntegerField(unique=True)
    def __str__(self) -> str:
        return f"{self.nombre} {self.cuit}"

class Producto(models.Model):
    producto=models.CharField(max_length=50, unique=True)
    descripcion=models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.producto}: {self.descripcion}"

class Vendedor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"