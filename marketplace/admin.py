from django.contrib import admin
from .models import Producto, Categoria
# Register your models here.
admin.site.register(Categoria)

admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'propietario', 'estado', 'fecha_publicacion', 'categoria')
    list_filter = ('estado', 'fecha_publicacion', 'categoria')
    search_fields = ('titulo', 'descripcion')
