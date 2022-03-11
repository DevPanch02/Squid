from django.db import models

class Paginas(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'una página'
        verbose_name_plural = 'varias páginas'
        db_table='pagina'
        ordering = ['id']
