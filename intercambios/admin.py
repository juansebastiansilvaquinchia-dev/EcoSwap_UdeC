from django.contrib import admin
from .models import PropuestaTrueque

# Register your models here.
@admin.register(PropuestaTrueque)
class PropuestaTruequeAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario_ofertante', 'usuario_receptor','estado', 'fecha_creacion')
    list_filter = ('estado',)
    