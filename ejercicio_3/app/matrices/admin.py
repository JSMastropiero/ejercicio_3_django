from django.contrib import admin
from .models import Matriz

@admin.register(Matriz)
class MatrizAdmin(admin.ModelAdmin):
    list_display = ('id', 'filas', 'columnas', 'creado_el')
    search_fields = ('id', 'filas', 'columnas')


