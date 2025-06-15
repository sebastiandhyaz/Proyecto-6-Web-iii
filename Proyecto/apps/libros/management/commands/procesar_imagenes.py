from django.core.management.base import BaseCommand
from apps.libros.models import Libro
from PIL import Image
import os

class Command(BaseCommand):
    help = 'Procesa todas las imágenes de libros a 1080x1920'

    def handle(self, *args, **options):
        libros = Libro.objects.filter(portada__isnull=False)
        
        self.stdout.write(f'📚 Encontrados {libros.count()} libros con imagen')
        
        for libro in libros:
            try:
                self.stdout.write(f'🔄 Procesando: {libro.titulo}')
                
                if not os.path.exists(libro.portada.path):
                    self.stdout.write(f'❌ Archivo no existe: {libro.portada.path}')
                    continue
                
                # Mostrar tamaño actual
                with Image.open(libro.portada.path) as img:
                    self.stdout.write(f'📐 Tamaño actual: {img.size}')
                
                # Procesar imagen
                libro.resize_image()
                
                # Mostrar nuevo tamaño
                with Image.open(libro.portada.path) as img:
                    self.stdout.write(f'✅ Nuevo tamaño: {img.size}')
                
            except Exception as e:
                self.stdout.write(f'❌ Error procesando {libro.titulo}: {e}')
        
        self.stdout.write('🎉 Procesamiento completado!')
