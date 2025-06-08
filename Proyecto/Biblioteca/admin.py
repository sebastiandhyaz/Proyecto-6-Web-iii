from django.contrib import admin
from .models import Libro, Socio, Prestamo, Multa

admin.site.register(Libro)
admin.site.register(Socio)
admin.site.register(Prestamo)
admin.site.register(Multa)
