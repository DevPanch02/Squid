from datetime import datetime
from email.policy import default
from django.db import models
from core.category.models import Categoria

estado = (
    ("activo","activo"),
    ("inactivo","inactivo"),
)

class Producto(models.Model):
    categoriaName=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria Name')
    nombre=models.CharField(max_length=30, verbose_name='Nombre')
    apellido=models.CharField(max_length=30, verbose_name='Apellido')
    direccion=models.CharField(max_length=30, verbose_name='Direccion')
    email=models.CharField(max_length=30, verbose_name='Username',unique=True)
    password=models.CharField(max_length=30, verbose_name='Contrasenia')
    #date_joined=models.DateField(default=datetime.now, verbose_name='fecha de registro')
    estado=models.CharField(max_length=20,choices=estado, default=1)
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table='usuarios'
        ordering = ['id']

