from django.contrib import admin
from .models import Student
# Register your models here.
from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('document_type', 'document_number', 'code', 'first_name', 'last_name', 'email')
    search_fields = ('document_type', 'document_number', 'code', 'first_name', 'last_name', 'email')