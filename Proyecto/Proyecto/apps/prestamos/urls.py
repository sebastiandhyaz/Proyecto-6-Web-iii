from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_prestamos, name='lista_prestamos'),
    path('nuevo/', views.nuevo_prestamo, name='nuevo_prestamo'),
    path('nuevo/modal/', views.nuevo_prestamo_modal, name='nuevo_prestamo_modal'),
    path('<int:pk>/', views.detalle_prestamo, name='detalle_prestamo'),
    path('<int:pk>/editar/', views.editar_prestamo, name='editar_prestamo'),
    path('<int:pk>/eliminar/', views.eliminar_prestamo, name='eliminar_prestamo'),
    path('<int:pk>/devolver/', views.devolver_prestamo, name='devolver_prestamo'),
    path('<int:pk>/renovar/', views.renovar_prestamo, name='renovar_prestamo'),
]
