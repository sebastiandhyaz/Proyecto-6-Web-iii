from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_prestamos, name='lista_prestamos'),
    path('nuevo/', views.nuevo_prestamo, name='nuevo_prestamo'),
    path('<int:pk>/', views.detalle_prestamo, name='detalle_prestamo'),
    path('<int:pk>/devolver/', views.devolver_prestamo, name='devolver_prestamo'),
    path('<int:pk>/renovar/', views.renovar_prestamo, name='renovar_prestamo'),
]
