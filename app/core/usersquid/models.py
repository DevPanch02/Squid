from datetime import datetime
from email.policy import default
from django.db import models
from core.category.models import Categoria
from django.utils import timezone

estado = (
    ("1","activo"),
    ("0","inactivo"),
)

def get_default_fecha():
    fecha = timezone.now()
    formatFecha = fecha.strftime("%Y/%m/%d %H:%M:%S")
    return formatFecha

class Usersquid(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    username=models.CharField(max_length=100, verbose_name='Nombre de usuario', unique=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombres')
    apellido=models.CharField(max_length=100, verbose_name='Apellidos')
    direccion=models.CharField(max_length=100, verbose_name='Dirección')
    email=models.CharField(max_length=100, verbose_name='Email', unique=True)
    password=models.CharField(max_length=100, verbose_name='Contraseña')
    registro=models.DateTimeField(verbose_name='Registrado el', auto_now_add=True)
    actualizacion=models.DateTimeField(verbose_name='Última actualización', auto_now=True)
    accedio=models.DateTimeField(verbose_name='último inicio de sesión', null=True, blank=True)
    estado=models.CharField(max_length=20,choices=estado, default=1, verbose_name="Estado")
    

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'un usuario'
        verbose_name_plural = 'varios usuarios'
        db_table='usersquid'
        ordering = ['id']