from django.contrib import admin
from django.urls import path

admin.autodiscover()  # Autodescubre los modelos registrados en el admin

urlpatterns = [
    path("admin/", admin.site.urls),  # Ruta para el administrador de Django
]
