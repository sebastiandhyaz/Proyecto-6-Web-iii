from django.db import models

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    activo = models.BooleanField(default=True)
    fecha_alta = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    stock_disponible = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField()
    renovaciones = models.PositiveIntegerField(default=0)
    devuelto = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.socio} - {self.libro}"

class Multa(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_multa = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Pendiente')
    def __str__(self):
        return f"Multa {self.id} - {self.socio}"
