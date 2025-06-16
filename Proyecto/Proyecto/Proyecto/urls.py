"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Proyecto.views_dashboard import dashboard_stats

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),  # Login/Register y home
    path("estadisticas/", include("apps.estadisticas.urls")),
    path("socios/", include("apps.socios.urls")),
    path("libros/", include("apps.libros.urls")),
    path("prestamos/", include("apps.prestamos.urls")),
    path("multas/", include("apps.multas.urls")),
    path('admin/', admin.site.urls),
    path('configuracion/', include('apps.configuracion.urls')),
    path("api/dashboard-stats/", dashboard_stats, name="dashboard_stats"),
]

# Servir archivos de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
