from django.db import models
from apps.socios.models import Socio
from apps.libros.models import Libro

class Prestamo(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name='prestamos')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion_estimada = models.DateField()
    fecha_devolucion_real = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('vencido', 'Vencido'), ('finalizado', 'Finalizado')], default='activo')
    renovado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.libro} a {self.socio} ({self.estado})"
