from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_multas, name='lista_multas'),
    path('nueva/', views.nueva_multa, name='nueva_multa'),
    path('nueva/modal/', views.nueva_multa_modal, name='nueva_multa_modal'),
    path('<int:pk>/', views.detalle_multa, name='detalle_multa'),
    path('<int:pk>/editar/', views.editar_multa, name='editar_multa'),
    path('<int:pk>/eliminar/', views.eliminar_multa, name='eliminar_multa'),
    path('<int:pk>/pagar/', views.pagar_multa, name='pagar_multa'),
    path('<int:pk>/anular/', views.anular_multa, name='anular_multa'),
]
