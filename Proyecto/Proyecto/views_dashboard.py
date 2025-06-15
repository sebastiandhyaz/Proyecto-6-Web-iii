from django.http import JsonResponse
from apps.socios.models import Socio
from apps.libros.models import Libro
from apps.prestamos.models import Prestamo
from apps.multas.models import Multa
from django.db.models import Sum, Count

def dashboard_stats(request):
    data = {
        'libros': Libro.objects.count(),
        'prestamos': Prestamo.objects.filter(estado='activo').count(),
        'socios': Socio.objects.filter(estado='activo').count(),
        'multas': float(Multa.objects.filter(pagada=False, anulada=False).aggregate(total=Sum('monto'))['total'] or 0),
        'libros_por_categoria': list(Libro.objects.values('categoria').annotate(total=Sum('cantidad'))),
        'prestamos_por_mes': list(Prestamo.objects.extra({'mes': "strftime('%%Y-%%m', fecha_prestamo)"}).values('mes').annotate(total=Sum('id'))),
        'socios_por_estado': list(Socio.objects.values('estado').annotate(total=Count('id'))),
    }
    return JsonResponse(data)
