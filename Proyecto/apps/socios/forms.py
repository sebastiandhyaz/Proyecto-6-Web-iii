from django import forms
from django.contrib.auth.models import User
from .models import Socio

class SocioForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, required=True, label="Nombre")
    apellido = forms.CharField(max_length=100, required=False, label="Apellido")
    email = forms.EmailField(required=True, label="Email")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")
    direccion = forms.CharField(max_length=255, required=False, label="Dirección")

    class Meta:
        model = Socio
        fields = ['telefono', 'direccion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.user:
            self.fields['nombre'].initial = self.instance.user.first_name
            self.fields['apellido'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        socio = super().save(commit=False)
        if commit:
            socio.save()
        return socio
