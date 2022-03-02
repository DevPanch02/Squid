from django.db import models
from core.products.models import *

class Paginas(models.Model):
    usuario=models.ForeignKey(Producto, on_delete=models.CASCADE)
    paginas=models.CharField(max_length=50, verbose_name='Ingrese pagina a visitar')

    def __str__(self):
        return self.paginas

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        db_table='pagina'
        ordering = ['id']
