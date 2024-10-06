from django.db import models
from apiPedidos.Usuario.domain.models import Usuario
from apiPedidos.DireccionEnvio.domain.models import DireccionEnvio
from enum import Enum
class EstadoPedido(Enum):
    CREADO = 'Creado'
    PENDIENTE = 'Pendiente'
    ENVIADO = 'Enviado'
    ENTREGADO = 'Entregado'
    CANCELADO = 'Cancelado'

EstadoPedidoChoices = [(tag.name, tag.value) for tag in EstadoPedido]

class Pedido(models.Model):
    pedidoId = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    direccion = models.ForeignKey(DireccionEnvio, on_delete=models.CASCADE, related_name='pedidos')
    fechaPedido = models.DateTimeField(auto_now_add=True)
    fechaEntrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=50,
                              choices=EstadoPedidoChoices,
                              default=EstadoPedido.CREADO.value)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    observaciones = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.pedidoId