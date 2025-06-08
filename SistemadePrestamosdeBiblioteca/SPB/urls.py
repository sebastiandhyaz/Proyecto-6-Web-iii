from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    # Socios
    path('socios/', views.socios_view, name='socios'),
    path('socios/registrar/', views.registrar_socio_view, name='registrar_socio'),
    path('socios/lista/', views.lista_socios_view, name='lista_socios'),
    path('prestamos/historial/', views.historial_prestamos_view, name='historial_prestamos'),
    # Libros
    path('libros/', views.libros_view, name='libros'),
    path('libros/registrar/', views.registrar_libro_view, name='registrar_libro'),
    path('libros/lista/', views.lista_libros_view, name='lista_libros'),
    # Préstamos
    path('prestamos/', views.prestamos_view, name='prestamos'),
    path('prestamos/registrar/', views.registrar_prestamo_view, name='registrar_prestamo'),
    path('prestamos/lista/', views.lista_prestamos_view, name='lista_prestamos'),
    # Multas
    path('multas/', views.multas_view, name='multas'),
    path('multas/registrar/', views.registrar_multa_view, name='registrar_multa'),
    path('multas/lista/', views.lista_multas_view, name='lista_multas'),
]
