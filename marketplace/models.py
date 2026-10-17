from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre de la categoría')
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    ESTADO_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ("Semi", 'Semi-nuevo / Poco uso'),
        ('Usado', 'Usado en buen estado'),
        ("DETALLES", 'Usado con detalles / Funcional'),
    ]  


# atributos del modelo
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos')
    titulo = models.CharField(max_length=100, verbose_name='Título del producto')
    descripcion = models.TextField(verbose_name='Descripción detallada del producto')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='USADO')
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')

    def __str__(self):
        return f"{self.titulo}-{self.get_estado_display()}"