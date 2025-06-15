from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Socio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='socio')
    fecha_alta = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('bloqueado', 'Bloqueado'), ('inactivo', 'Inactivo')], default='activo')
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    bloqueado_por_multas = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
