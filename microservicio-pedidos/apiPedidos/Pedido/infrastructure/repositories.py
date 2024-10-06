from apiPedidos.Pedido.domain.models import Pedido
from apiPedidos.Pedido.exceptions.Pedido_exceptions import PedidoNotFound, InvalidPedidoException, UsuarioNotFoundPedido, DireccionNotFoundPedido

class PedidoRepository:

    @staticmethod
    def savePedido(pedido):
        pedido.save()
    
    @staticmethod
    def getPedidoById(pedidoId):
        try:
            return Pedido.objects.get(pedidoId=pedidoId)
        except Pedido.DoesNotExist:
            return None
    
    @staticmethod
    def getPedidosByUserId(idUsuario):
        try:
            return Pedido.objects.filter(usuario__idUsuario=idUsuario)
        except Pedido.DoesNotExist:
            return None
        
    @staticmethod
    def getPeidosByUserIdAndEstado(idUsuario, estado):
        try:
            return Pedido.objects.filter(usuario__idUsuario=idUsuario, estado=estado)
        except Pedido.DoesNotExist:
            return None
        
    @staticmethod
    def getPedidoByUserIdAndPedidoId(idUsuario, pedidoId):
        try:
            return Pedido.objects.get(usuario__idUsuario=idUsuario, pedidoId=pedidoId)
        except Pedido.DoesNotExist:
            return None
        
    @staticmethod
    def getPedidoByUserIdAndFechaPedido(idUsuario, fechaPedidodesde, fechaPedidoHasta):
        try:
            return Pedido.objects.filter(usuario__idUsuario=idUsuario, fechaPedido__range=[fechaPedidodesde, fechaPedidoHasta])
        except Pedido.DoesNotExist:
            return None
    @staticmethod
    def getPedidosByEstado(estado):
        try:
            return Pedido.objects.filter(estado=estado)
        except Pedido.DoesNotExist:
            return None
    
    @staticmethod
    def getPedidosByRangeFechaPedido(fechaPedidodesde, fechaPedidoHasta):
        try:
            return Pedido.objects.filter(fechaPedido__range=[fechaPedidodesde, fechaPedidoHasta])
        except Pedido.DoesNotExist:
            return None
        
    @staticmethod
    def deletePedido(pedidoId):
        try:
            pedido = Pedido.objects.get(pedidoId=pedidoId)
            pedido.delete()
            return True
        except Pedido.DoesNotExist:
            return False
        
    @staticmethod
    def getPedidosByFechaPedido(fechaPedido):
        try:
            return Pedido.objects.filter(fechaPedido=fechaPedido)
        except Pedido.DoesNotExist:
            return None
    @staticmethod
    def getPedidosByFechaEntrega(fechaEntrega):
        try:
            return Pedido.objects.filter(fechaEntrega=fechaEntrega)
        except Pedido.DoesNotExist:
            return None