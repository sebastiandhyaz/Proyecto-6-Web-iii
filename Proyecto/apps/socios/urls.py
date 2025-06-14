from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_socios, name='lista_socios'),
    path('nuevo/', views.nuevo_socio, name='nuevo_socio'),
    path('<int:pk>/', views.detalle_socio, name='detalle_socio'),
    path('<int:pk>/editar/', views.editar_socio, name='editar_socio'),
    path('<int:pk>/bloquear/', views.bloquear_socio, name='bloquear_socio'),
    path('<int:pk>/eliminar/', views.eliminar_socio, name='eliminar_socio'),
]
