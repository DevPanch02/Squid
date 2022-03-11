from django.db import models

class Categoria(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='Nombre', unique=True)

    def __str__(self) :
        return self.nombre

    class Meta:
        verbose_name = 'una categoria'
        verbose_name_plural = 'varias categorias'
        db_table='categoria'
        ordering = ['id']
