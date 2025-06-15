from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('nuevo/', views.nuevo_libro, name='nuevo_libro'),
    path('nuevo/modal/', views.nuevo_libro_modal, name='nuevo_libro_modal'),
    path('<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('<int:pk>/editar/', views.editar_libro, name='editar_libro'),
    path('<int:pk>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]
