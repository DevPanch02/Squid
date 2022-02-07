from django.db import models

class Categoria(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='Categoria', unique=True)

    def __str__(self) :
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table='categoria'
        ordering = ['id']
