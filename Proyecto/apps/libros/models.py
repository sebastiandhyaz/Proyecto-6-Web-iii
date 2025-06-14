from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    editorial = models.CharField(max_length=255)
    anio = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=1)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    descripcion = models.TextField(blank=True)
    disponibles = models.PositiveIntegerField(default=1)
    prestados = models.PositiveIntegerField(default=0)
    danados = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.titulo} ({self.autor})"
