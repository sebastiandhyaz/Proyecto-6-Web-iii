from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Socio
from .forms import SocioForm
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def lista_socios(request):
    query = request.GET.get('q', '')
    filtro = request.GET.get('filtro', '')
    socios = Socio.objects.all()
    if query:
        socios = socios.filter(Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query) | Q(user__email__icontains=query))
    if filtro:
        if filtro == 'activos':
            socios = socios.filter(estado='activo')
        elif filtro == 'bloqueados':
            socios = socios.filter(estado='bloqueado')
        elif filtro == 'multas':
            socios = socios.filter(bloqueado_por_multas=True)
    return render(request, 'socios/lista_socios.html', {'socios': socios, 'query': query, 'filtro': filtro})

@login_required
def nuevo_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Ya existe un usuario con ese email.')
            else:
                user = User.objects.create_user(username=email, email=email, first_name=form.cleaned_data['nombre'])
                socio = form.save(commit=False)
                socio.user = user
                socio.save()
                messages.success(request, 'Socio registrado correctamente.')
                return redirect('lista_socios')
    else:
        form = SocioForm()
    return render(request, 'socios/nuevo_socio_form.html', {'form': form})

@login_required
def detalle_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    # Aquí se pueden agregar préstamos, multas, historial, etc.
    return render(request, 'socios/detalle_socio.html', {'socio': socio})

@login_required
def editar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos actualizados.')
            return redirect('detalle_socio', pk=socio.pk)
    else:
        form = SocioForm(instance=socio)
    return render(request, 'socios/editar_socio.html', {'form': form, 'socio': socio})

@login_required
def bloquear_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    socio.estado = 'bloqueado'
    socio.save()
    messages.success(request, 'Socio bloqueado.')
    return redirect('detalle_socio', pk=pk)

@login_required
def eliminar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    socio.user.delete()
    socio.delete()
    messages.success(request, 'Socio eliminado.')
    return redirect('lista_socios')

@login_required
def nuevo_socio_modal(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data.get('apellido', '')
            
            # Verificar si ya existe un usuario con ese email
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Ya existe un usuario con ese email.')
                html = render_to_string('socios/nuevo_socio_form.html', {'form': form}, request=request)
                return JsonResponse({'success': False, 'form_html': html})
            
            # Crear el usuario
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=nombre,
                last_name=apellido
            )
            
            # Crear el socio
            socio = form.save(commit=False)
            socio.user = user
            socio.save()
            
            html = render_to_string('socios/socio_row.html', {'socio': socio}, request=request)
            return JsonResponse({'success': True, 'html': html})
        else:
            html = render_to_string('socios/nuevo_socio_form.html', {'form': form}, request=request)
            return JsonResponse({'success': False, 'form_html': html})
    else:
        form = SocioForm()
        html = render_to_string('socios/nuevo_socio_form.html', {'form': form}, request=request)
        return JsonResponse({'form_html': html})
