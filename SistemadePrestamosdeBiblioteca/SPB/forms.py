from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Socio, Libro, Prestamo, Multa

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('El email ya está registrado.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Las contraseñas no coinciden.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'apellido', 'dni', 'email', 'telefono', 'direccion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'dni': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'editorial', 'stock_disponible']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'autor': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'stock_disponible': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
        }

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['socio', 'libro', 'fecha_devolucion', 'renovaciones', 'devuelto']
        widgets = {
            'socio': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'libro': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'fecha_devolucion': forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'}),
            'renovaciones': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'devuelto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MultaForm(forms.ModelForm):
    class Meta:
        model = Multa
        fields = ['socio', 'prestamo', 'monto', 'estado']
        widgets = {
            'socio': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'prestamo': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'estado': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }
