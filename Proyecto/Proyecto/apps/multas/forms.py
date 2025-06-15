from django import forms
from .models import Multa
from apps.prestamos.models import Prestamo
from apps.socios.models import Socio

class MultaForm(forms.ModelForm):
    prestamo = forms.ModelChoiceField(queryset=Prestamo.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    socio = forms.ModelChoiceField(queryset=Socio.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    monto = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    class Meta:
        model = Multa
        fields = ['prestamo', 'socio', 'monto', 'motivo']
