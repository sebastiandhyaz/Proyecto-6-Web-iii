from django import forms
from .models import Multa

class MultaForm(forms.ModelForm):
    class Meta:
        model = Multa
        fields = ['prestamo', 'socio', 'monto', 'motivo']
