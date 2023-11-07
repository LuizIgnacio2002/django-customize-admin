from django.contrib import admin
from django.urls import path
from .models import Student  # Importa el modelo Student

admin.site.register(Student)  # Registra el modelo Student en el admin de Django

urlpatterns = [
    path("admin/", admin.site.urls),  # Ruta para el administrador de Django
]