from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_multas, name='lista_multas'),
    path('nueva/', views.nueva_multa, name='nueva_multa'),
    path('<int:pk>/', views.detalle_multa, name='detalle_multa'),
    path('<int:pk>/pagar/', views.pagar_multa, name='pagar_multa'),
    path('<int:pk>/anular/', views.anular_multa, name='anular_multa'),
]
