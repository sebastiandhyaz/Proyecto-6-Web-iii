from django import forms
from .models import Prestamo
from apps.socios.models import Socio
from apps.libros.models import Libro

class PrestamoForm(forms.ModelForm):
    socio = forms.ModelChoiceField(queryset=Socio.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_devolucion_estimada = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    class Meta:
        model = Prestamo
        fields = ['socio', 'libro', 'fecha_devolucion_estimada']
