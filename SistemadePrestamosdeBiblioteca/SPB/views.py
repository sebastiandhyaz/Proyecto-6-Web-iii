from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, SocioForm, LibroForm, PrestamoForm, MultaForm
from django.views.decorators.csrf import csrf_protect
from .models import Socio, Libro, Prestamo, Multa

@csrf_protect
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@csrf_protect
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='/login/')
def dashboard_view(request):
    total_socios = Socio.objects.count()
    total_libros = Libro.objects.count()
    prestamos_activos = Prestamo.objects.filter(devuelto=False).count()
    multas_pendientes = Multa.objects.filter(estado__iexact='Pendiente').count()
    return render(request, 'dashboard.html', {
        'total_socios': total_socios,
        'total_libros': total_libros,
        'prestamos_activos': prestamos_activos,
        'multas_pendientes': multas_pendientes,
    })

@login_required(login_url='/login/')
def socios_view(request):
    return render(request, 'socios.html')

@login_required(login_url='/login/')
def registrar_socio_view(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Socio registrado correctamente.')
            return redirect('socios')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = SocioForm()
    return render(request, 'registrar_socio.html', {'form': form})

@login_required(login_url='/login/')
def lista_socios_view(request):
    socios = Socio.objects.all()
    return render(request, 'lista_socios.html', {'socios': socios})

@login_required(login_url='/login/')
def historial_prestamos_view(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'historial_prestamos.html', {'prestamos': prestamos})

@login_required(login_url='/login/')
def libros_view(request):
    return render(request, 'libros.html')

@login_required(login_url='/login/')
def prestamos_view(request):
    return render(request, 'prestamos.html')

@login_required(login_url='/login/')
def registrar_prestamo_view(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Préstamo registrado correctamente.')
            return redirect('lista_prestamos')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = PrestamoForm()
    return render(request, 'registrar_prestamo.html', {'form': form})

@login_required(login_url='/login/')
def lista_prestamos_view(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'lista_prestamos.html', {'prestamos': prestamos})

@login_required(login_url='/login/')
def multas_view(request):
    return render(request, 'multas.html')

@login_required(login_url='/login/')
def registrar_multa_view(request):
    if request.method == 'POST':
        form = MultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Multa registrada correctamente.')
            return redirect('lista_multas')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = MultaForm()
    return render(request, 'registrar_multa.html', {'form': form})

@login_required(login_url='/login/')
def lista_multas_view(request):
    multas = Multa.objects.all()
    return render(request, 'lista_multas.html', {'multas': multas})
