from django.urls import path
from .views import perfil_view
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('socios/', views.lista_socios, name='lista_socios'),
    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('multas/', views.lista_multas, name='lista_multas'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('socios/crear/', views.crear_socio, name='crear_socio'),
    path('prestamos/crear/', views.crear_prestamo, name='crear_prestamo'),
    path('multas/crear/', views.crear_multa, name='crear_multa'),
    path('socios/<int:socio_id>/editar/', views.editar_socio, name='editar_socio'),
    path('socios/<int:socio_id>/eliminar/', views.eliminar_socio, name='eliminar_socio'),
    path('libros/<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    path('prestamos/<int:prestamo_id>/editar/', views.editar_prestamo, name='editar_prestamo'),
    path('prestamos/<int:prestamo_id>/eliminar/', views.eliminar_prestamo, name='eliminar_prestamo'),
    path('multas/<int:multa_id>/editar/', views.editar_multa, name='editar_multa'),
    path('multas/<int:multa_id>/eliminar/', views.eliminar_multa, name='eliminar_multa'),
    path('perfil/', views.perfil_view, name='perfil'),
    
]
