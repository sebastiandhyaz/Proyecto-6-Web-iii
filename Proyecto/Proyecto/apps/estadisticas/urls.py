from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('exportar/', views.exportar_estadisticas, name='exportar_estadisticas'),
]
