from datetime import datetime
from django.db import models
from core.category.models import Categoria

class Producto(models.Model):
    categoriaName=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria Name')
    nombre=models.CharField(max_length=30, verbose_name='Nombre')
    apellido=models.CharField(max_length=30, verbose_name='Apellido')
    direccion=models.CharField(max_length=30, verbose_name='Direccion')
    email=models.CharField(max_length=30, verbose_name='Email')
    password=models.CharField(max_length=30, verbose_name='Contrasenia')
    


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table='producto'
        ordering = ['id']