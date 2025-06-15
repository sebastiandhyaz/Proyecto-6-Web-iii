from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Prestamo
from .forms import PrestamoForm
from django.db.models import Q
from datetime import date
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def lista_prestamos(request):
    query = request.GET.get('q', '')
    filtro = request.GET.get('filtro', '')
    prestamos = Prestamo.objects.select_related('socio', 'libro').all()
    if query:
        prestamos = prestamos.filter(Q(socio__user__first_name__icontains=query) | Q(libro__titulo__icontains=query))
    if filtro:
        if filtro == 'activos':
            prestamos = prestamos.filter(estado='activo')
        elif filtro == 'vencidos':
            prestamos = prestamos.filter(estado='vencido')
        elif filtro == 'finalizados':
            prestamos = prestamos.filter(estado='finalizado')
    return render(request, 'prestamos/lista_prestamos.html', {'prestamos': prestamos, 'query': query, 'filtro': filtro})

@login_required
def nuevo_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            if prestamo.libro.disponibles < 1:
                messages.error(request, 'No hay ejemplares disponibles.')
            else:
                prestamo.save()
                prestamo.libro.disponibles -= 1
                prestamo.libro.prestados += 1
                prestamo.libro.save()
                messages.success(request, 'Préstamo registrado correctamente.')
                return redirect('lista_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'prestamos/nuevo_prestamo_form.html', {'form': form})

@login_required
def detalle_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    return render(request, 'prestamos/detalle_prestamo.html', {'prestamo': prestamo})

@login_required
def devolver_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if not prestamo.fecha_devolucion_real:
        prestamo.fecha_devolucion_real = date.today()
        prestamo.estado = 'finalizado'
        prestamo.libro.disponibles += 1
        prestamo.libro.prestados -= 1
        prestamo.libro.save()
        prestamo.save()
        messages.success(request, 'Préstamo devuelto correctamente.')
    return redirect('detalle_prestamo', pk=pk)

@login_required
def renovar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if not prestamo.renovado and prestamo.estado == 'activo':
        prestamo.renovado = True
        prestamo.fecha_devolucion_estimada = prestamo.fecha_devolucion_estimada.replace(day=prestamo.fecha_devolucion_estimada.day+7)
        prestamo.save()
        messages.success(request, 'Préstamo renovado por 7 días.')
    else:
        messages.error(request, 'No se puede renovar este préstamo.')
    return redirect('detalle_prestamo', pk=pk)

@login_required
def nuevo_prestamo_modal(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            if prestamo.libro.disponibles < 1:
                html = render_to_string('prestamos/nuevo_prestamo_form.html', {'form': form}, request=request)
                return JsonResponse({'success': False, 'form_html': html, 'error': 'No hay ejemplares disponibles.'})
            else:
                prestamo.save()
                prestamo.libro.disponibles -= 1
                prestamo.libro.prestados += 1
                prestamo.libro.save()
                html = render_to_string('prestamos/prestamo_row.html', {'prestamo': prestamo}, request=request)
                return JsonResponse({'success': True, 'html': html})
        else:
            html = render_to_string('prestamos/nuevo_prestamo_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'form_html': html})
    else:
        form = PrestamoForm()
        html = render_to_string('prestamos/nuevo_prestamo_form.html', {'form': form}, request=request)
        return JsonResponse({'form_html': html})

@login_required
def editar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Préstamo actualizado correctamente.')
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'prestamos/editar_prestamo.html', {'form': form, 'prestamo': prestamo})

@login_required
def eliminar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        # Restaurar disponibilidad del libro
        prestamo.libro.disponibles += 1
        prestamo.libro.prestados -= 1
        prestamo.libro.save()
        prestamo.delete()
        messages.success(request, 'Préstamo eliminado correctamente.')
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
