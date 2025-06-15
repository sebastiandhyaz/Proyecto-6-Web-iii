from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Libro
from .forms import LibroForm
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def lista_libros(request):
    query = request.GET.get('q', '')
    filtro = request.GET.get('filtro', '')
    libros = Libro.objects.all()
    if query:
        libros = libros.filter(Q(titulo__icontains=query) | Q(autor__icontains=query) | Q(isbn__icontains=query) | Q(categoria__icontains=query))
    if filtro:
        if filtro == 'disponibles':
            libros = libros.filter(disponibles__gt=0)
        elif filtro == 'prestados':
            libros = libros.filter(prestados__gt=0)
        elif filtro == 'nuevos':
            libros = libros.order_by('-id')[:10]
    return render(request, 'libros/lista_libros.html', {'libros': libros, 'query': query, 'filtro': filtro})

@login_required
def nuevo_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save()
            # Forzar el procesamiento de imagen si se subió una
            if libro.portada:
                print(f"🔄 Procesando imagen para libro: {libro.titulo}")
                libro.resize_image()
            messages.success(request, 'Libro agregado correctamente.')
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/nuevo_libro_form.html', {'form': form})

@login_required
def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})

@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            # Verificar si se subió una nueva imagen
            imagen_anterior = libro.portada
            libro_actualizado = form.save()
            
            # Si cambió la imagen, procesarla
            if libro_actualizado.portada and libro_actualizado.portada != imagen_anterior:
                print(f"🔄 Procesando nueva imagen para libro: {libro_actualizado.titulo}")
                libro_actualizado.resize_image()
                
            messages.success(request, 'Datos del libro actualizados.')
            return redirect('detalle_libro', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form, 'libro': libro})

@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    libro.delete()
    messages.success(request, 'Libro eliminado.')
    return redirect('lista_libros')

@login_required
def nuevo_libro_modal(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save()
            html = render_to_string('libros/libro_row.html', {'libro': libro}, request=request)
            return JsonResponse({'success': True, 'html': html})
        else:
            html = render_to_string('libros/nuevo_libro_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'form_html': html})
    else:
        form = LibroForm()
        html = render_to_string('libros/nuevo_libro_form.html', {'form': form}, request=request)
        return JsonResponse({'form_html': html})
