from django.db import models
from apps.prestamos.models import Prestamo
from apps.socios.models import Socio

class Multa(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name='multas')
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name='multas')
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    motivo = models.CharField(max_length=255)
    fecha_generada = models.DateField(auto_now_add=True)
    pagada = models.BooleanField(default=False)
    fecha_pago = models.DateField(blank=True, null=True)
    anulada = models.BooleanField(default=False)
    justificacion_anulacion = models.TextField(blank=True)

    def __str__(self):
        return f"Multa {self.monto} - {self.socio} ({'Pagada' if self.pagada else 'Impaga'})"
