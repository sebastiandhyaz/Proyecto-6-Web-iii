from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib import messages
from .forms import CustomUserCreationForm

def login_register(request):
    login_form = AuthenticationForm()
    register_form = CustomUserCreationForm()
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, 'Bienvenido, sesión iniciada correctamente.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        elif 'register' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                messages.success(request, 'Registro exitoso. ¡Bienvenido!')
                return redirect('dashboard')
            else:
                for field, errors in register_form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
    return render(request, 'users/login_register.html', {
        'form': login_form,
        'reg_form': register_form
    })

def logout_view(request):
    logout(request)
    return redirect('login_register')

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'Se ha enviado un correo para restablecer la contraseña.')
            return redirect('login_register')
    else:
        form = PasswordResetForm()
    return render(request, 'users/password_reset.html', {'form': form})
