from django import forms
from django.contrib.auth.models import User
from .models import Socio

class SocioForm(forms.ModelForm):
    nombre = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Socio
        fields = ['telefono', 'direccion']

    def save(self, commit=True):
        socio = super().save(commit=False)
        if commit:
            socio.save()
        return socio
