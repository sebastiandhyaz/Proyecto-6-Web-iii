from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import UserRegisterForm, SocioForm, LibroForm, PrestamoForm, MultaForm
from django.contrib.auth.forms import AuthenticationForm
from Biblioteca.models import Libro, Prestamo, Socio, Multa
from django.db import models

@csrf_protect
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

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

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

@login_required(login_url='/login/')
def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'lista_socios.html', {'socios': socios})

@login_required(login_url='/login/')
def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'lista_prestamos.html', {'prestamos': prestamos})

@login_required(login_url='/login/')
def lista_multas(request):
    multas = Multa.objects.all()
    return render(request, 'lista_multas.html', {'multas': multas})

@login_required(login_url='/login/')
def crear_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Socio creado correctamente.')
            return redirect('lista_socios')
    else:
        form = SocioForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Socio'})

@login_required(login_url='/login/')
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado correctamente.')
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Libro'})

@login_required(login_url='/login/')
def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Préstamo creado correctamente.')
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Préstamo'})

@login_required(login_url='/login/')
def crear_multa(request):
    if request.method == 'POST':
        form = MultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Multa creada correctamente.')
            return redirect('lista_multas')
    else:
        form = MultaForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Multa'})

@login_required(login_url='/login/')
def editar_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Socio actualizado correctamente.')
            return redirect('lista_socios')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar Socio'})

@login_required(login_url='/login/')
def eliminar_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    if request.method == 'POST':
        socio.delete()
        messages.success(request, 'Socio eliminado correctamente.')
        return redirect('lista_socios')
    return render(request, 'confirmar_eliminar.html', {'objeto': socio, 'tipo': 'Socio'})

@login_required(login_url='/login/')
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado correctamente.')
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar Libro'})

@login_required(login_url='/login/')
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado correctamente.')
        return redirect('lista_libros')
    return render(request, 'confirmar_eliminar.html', {'objeto': libro, 'tipo': 'Libro'})

@login_required(login_url='/login/')
def editar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Préstamo actualizado correctamente.')
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar Préstamo'})

@login_required(login_url='/login/')
def eliminar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)
    if request.method == 'POST':
        prestamo.delete()
        messages.success(request, 'Préstamo eliminado correctamente.')
        return redirect('lista_prestamos')
    return render(request, 'confirmar_eliminar.html', {'objeto': prestamo, 'tipo': 'Préstamo'})

@login_required(login_url='/login/')
def editar_multa(request, multa_id):
    multa = get_object_or_404(Multa, id=multa_id)
    if request.method == 'POST':
        form = MultaForm(request.POST, instance=multa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Multa actualizada correctamente.')
            return redirect('lista_multas')
    else:
        form = MultaForm(instance=multa)
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar Multa'})

@login_required(login_url='/login/')
def eliminar_multa(request, multa_id):
    multa = get_object_or_404(Multa, id=multa_id)
    if request.method == 'POST':
        multa.delete()
        messages.success(request, 'Multa eliminada correctamente.')
        return redirect('lista_multas')
    return render(request, 'confirmar_eliminar.html', {'objeto': multa, 'tipo': 'Multa'})
