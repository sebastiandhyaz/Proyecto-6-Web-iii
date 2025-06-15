from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Multa
from .forms import MultaForm
from django.db.models import Q
from datetime import date
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def lista_multas(request):
    query = request.GET.get('q', '')
    filtro = request.GET.get('filtro', '')
    multas = Multa.objects.select_related('socio', 'prestamo').all()
    if query:
        multas = multas.filter(Q(socio__user__first_name__icontains=query) | Q(prestamo__libro__titulo__icontains=query))
    if filtro:
        if filtro == 'impagas':
            multas = multas.filter(pagada=False, anulada=False)
        elif filtro == 'pagadas':
            multas = multas.filter(pagada=True)
        elif filtro == 'anuladas':
            multas = multas.filter(anulada=True)
    return render(request, 'multas/lista_multas.html', {'multas': multas, 'query': query, 'filtro': filtro})

@login_required
def detalle_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    return render(request, 'multas/detalle_multa.html', {'multa': multa})

@login_required
def pagar_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    if not multa.pagada:
        multa.pagada = True
        multa.fecha_pago = date.today()
        multa.save()
        messages.success(request, 'Multa pagada correctamente.')
    return redirect('detalle_multa', pk=pk)

@login_required
def anular_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    if request.method == 'POST':
        justificacion = request.POST.get('justificacion', '')
        multa.anulada = True
        multa.justificacion_anulacion = justificacion
        multa.save()
        messages.success(request, 'Multa anulada.')
        return redirect('detalle_multa', pk=pk)
    return render(request, 'multas/anular_multa.html', {'multa': multa})

@login_required
def nueva_multa(request):
    if request.method == 'POST':
        form = MultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Multa generada correctamente.')
            return redirect('lista_multas')
    else:
        form = MultaForm()
    return render(request, 'multas/nueva_multa_form.html', {'form': form})

@login_required
def nueva_multa_modal(request):
    if request.method == 'POST':
        form = MultaForm(request.POST)
        if form.is_valid():
            multa = form.save()
            html = render_to_string('multas/multa_row.html', {'multa': multa}, request=request)
            return JsonResponse({'success': True, 'html': html})
        else:
            html = render_to_string('multas/nueva_multa_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'form_html': html})
    else:
        form = MultaForm()
        html = render_to_string('multas/nueva_multa_form.html', {'form': form}, request=request)
        return JsonResponse({'form_html': html})

@login_required
def editar_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    if request.method == 'POST':
        form = MultaForm(request.POST, instance=multa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Multa actualizada correctamente.')
            return redirect('lista_multas')
    else:
        form = MultaForm(instance=multa)
    return render(request, 'multas/editar_multa.html', {'form': form, 'multa': multa})

@login_required
def eliminar_multa(request, pk):
    multa = get_object_or_404(Multa, pk=pk)
    if request.method == 'POST':
        multa.delete()
        messages.success(request, 'Multa eliminada correctamente.')
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
