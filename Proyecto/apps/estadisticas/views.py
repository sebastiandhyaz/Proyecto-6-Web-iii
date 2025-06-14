from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.socios.models import Socio
from apps.libros.models import Libro
from apps.prestamos.models import Prestamo
from apps.multas.models import Multa
from django.db.models import Count, Sum
from datetime import datetime, timedelta

@login_required
def dashboard(request):
    # Tarjetas resumen
    total_libros = Libro.objects.count()
    prestamos_activos = Prestamo.objects.filter(estado='activo').count()
    socios_activos = Socio.objects.filter(estado='activo').count()
    multas_pendientes = Multa.objects.filter(pagada=False).aggregate(total=Sum('monto'))['total'] or 0

    # Gráfico de préstamos y devoluciones por mes (últimos 12 meses)
    hoy = datetime.today()
    meses = []
    prestamos_mes = []
    devoluciones_mes = []
    for i in range(11, -1, -1):
        mes = (hoy - timedelta(days=30*i)).strftime('%b %Y')
        prestamos = Prestamo.objects.filter(fecha_prestamo__month=(hoy - timedelta(days=30*i)).month).count()
        devoluciones = Prestamo.objects.filter(fecha_devolucion_real__month=(hoy - timedelta(days=30*i)).month).count()
        meses.append(mes)
        prestamos_mes.append(prestamos)
        devoluciones_mes.append(devoluciones)

    # Gráfico de libros por categoría
    categorias = list(Libro.objects.values_list('categoria', flat=True).distinct())
    libros_por_categoria = [Libro.objects.filter(categoria=cat).count() for cat in categorias]

    # Movimientos recientes
    movimientos = Prestamo.objects.select_related('socio', 'libro').order_by('-fecha_prestamo')[:10]

    # Alertas rápidas
    proximos_vencimientos = Prestamo.objects.filter(estado='activo', fecha_devolucion_estimada__lte=hoy+timedelta(days=3)).order_by('fecha_devolucion_estimada')[:5]
    multas_recientes = Multa.objects.filter(fecha_generada__gte=hoy-timedelta(days=7)).order_by('-fecha_generada')[:5]

    context = {
        'total_libros': total_libros,
        'prestamos_activos': prestamos_activos,
        'socios_activos': socios_activos,
        'multas_pendientes': multas_pendientes,
        'meses': meses,
        'prestamos_mes': prestamos_mes,
        'devoluciones_mes': devoluciones_mes,
        'categorias': categorias,
        'libros_por_categoria': libros_por_categoria,
        'movimientos': movimientos,
        'proximos_vencimientos': proximos_vencimientos,
        'multas_recientes': multas_recientes,
    }
    return render(request, 'estadisticas/dashboard.html', context)

@login_required
def exportar_estadisticas(request):
    # Lógica para exportar estadísticas a PDF/Excel
    pass
