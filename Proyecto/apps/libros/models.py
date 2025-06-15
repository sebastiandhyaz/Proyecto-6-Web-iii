from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os

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

    def save(self, *args, **kwargs):
        # Guardar primero para obtener el archivo
        super().save(*args, **kwargs)
        
        # Redimensionar imagen si existe y ha cambiado
        if self.portada and hasattr(self.portada, 'path'):
            self.resize_image()

    def resize_image(self):
        """Redimensiona la imagen a 1080x1920 con recorte inteligente"""
        try:
            # Abrir la imagen
            image = Image.open(self.portada.path)
            
            # Dimensiones objetivo: 1080x1920 (portrait)
            target_width = 1080
            target_height = 1920
            target_ratio = target_width / target_height  # ~0.5625
            
            # Convertir a RGB si es necesario
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")
            
            # Obtener dimensiones originales
            original_width, original_height = image.size
            original_ratio = original_width / original_height
            
            print(f"Procesando imagen: {original_width}x{original_height} (ratio: {original_ratio:.3f})")
            print(f"Objetivo: {target_width}x{target_height} (ratio: {target_ratio:.3f})")
            
            # Calcular dimensiones para recorte inteligente
            if original_ratio > target_ratio:
                # Imagen más ancha: ajustar por altura y recortar lados
                new_height = target_height
                new_width = int(target_height * original_ratio)
                print(f"Redimensionando a: {new_width}x{new_height}")
                resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Recortar desde el centro
                left = (new_width - target_width) // 2
                top = 0
                right = left + target_width
                bottom = target_height
                
            else:
                # Imagen más alta: ajustar por ancho y recortar arriba/abajo
                new_width = target_width
                new_height = int(target_width / original_ratio)
                print(f"Redimensionando a: {new_width}x{new_height}")
                resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Recortar desde el centro (favor hacia arriba para portadas)
                left = 0
                top = max(0, (new_height - target_height) // 4)  # Favor hacia arriba
                right = target_width
                bottom = top + target_height
            
            print(f"Recortando: left={left}, top={top}, right={right}, bottom={bottom}")
            
            # Aplicar el recorte
            cropped = resized.crop((left, top, right, bottom))
            
            # Verificar que el recorte es correcto
            print(f"Imagen final: {cropped.size}")
            
            # Guardar la imagen procesada
            cropped.save(self.portada.path, format='JPEG', quality=90, optimize=True)
            print("✅ Imagen procesada exitosamente")
            
        except Exception as e:
            print(f"❌ Error al redimensionar imagen: {e}")
            import traceback
            traceback.print_exc()

    def __str__(self):
        return f"{self.titulo} ({self.autor})"
