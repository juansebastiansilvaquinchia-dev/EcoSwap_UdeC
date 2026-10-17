from django.db import models
from django.contrib.auth.models import User
from marketplace.models import Producto

# Create your models here.

class PropuestaTrueque(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aceptada', 'Aceptada'),
        ('Rechazada', 'Rechazada'),
        ('Cancelada', 'Cancelada')
    ]

    # Usuario involucrados
    usuario_ofertante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="propuestas_enviadas")
    usuario_receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="propuestas_recibidas")

    # productos involucrados
    producto_ofrecido = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="ofertado_en")
    producto_solicitado = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="solicitado_en")

    # estado y fecha de la propuesta
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trueque #{self.id}: {self.usuario_ofertante.username} ofrece {self.producto_ofrecido.titulo} por {self.producto_solicitado.titulo}"