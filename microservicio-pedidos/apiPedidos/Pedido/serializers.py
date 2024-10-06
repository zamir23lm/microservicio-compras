from rest_framework import serializers
from apiPedidos.Usuario.domain.models import Usuario
from apiPedidos.DireccionEnvio.domain.models import DireccionEnvio
from apiPedidos.Pedido.domain.models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    direccion = serializers.PrimaryKeyRelatedField(queryset=DireccionEnvio.objects.all())
    pedidoId = serializers.IntegerField(required=False)
    class Meta:
        model = Pedido
        fields = [
            'pedidoId', 'usuario', 'direccion','fechaPedido','fechaEntrega', 'estado', 'total', 'observaciones'
        ]

class EditPedidoSerializer(serializers.ModelSerializer):
    fechaEntrega = serializers.DateTimeField(required=False)
    estado = serializers.CharField(required=False, max_length=50)
    total = serializers.DecimalField(max_digits=9, decimal_places=2, required=False, allow_null=True)
    observaciones = serializers.CharField(required=False, max_length=500)
    
    class Meta:
        model = Pedido
        fields = [
            'fechaEntrega', 'estado', 'total', 'observaciones'
        ]

class PedidoDtoSerializer(serializers.ModelSerializer):
    id_pedido = serializers.IntegerField()  
    id_cliente = serializers.IntegerField()
    id_direccion = serializers.IntegerField()
    fecha_pedido = serializers.DateTimeField()
    fecha_entrega = serializers.DateTimeField()
    estado_pedido = serializers.CharField(max_length=50)
    total_pedido = serializers.DecimalField(max_digits=9, decimal_places=2)
    observaciones = serializers.CharField(max_length=500)
    class Meta:
        model = Pedido
        fields = [
            'id_pedido', 'id_cliente', 'id_direccion', 'fecha_pedido', 'fecha_entrega', 'estado_pedido', 'total_pedido', 'observaciones'
        ]
class PedidoIdSerializer(serializers.ModelSerializer):
    pedidoId = serializers.IntegerField()
    class Meta:
        model = Pedido
        fields = [
            'pedidoId'
        ]