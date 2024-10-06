from rest_framework import serializers
from apiPedidos.Usuario.domain.services import UsuarioService
from apiPedidos.DireccionEnvio.domain.services import DireccionEnvioService
from apiPedidos.Pedido.domain.models import Pedido
from apiPedidos.Pedido.exceptions.Pedido_exceptions import PedidoNotFound, InvalidPedidoException, UsuarioNotFoundPedido, DireccionNotFoundPedido
from datetime import datetime, timedelta
from apiPedidos.Usuario.domain.models import Usuario
from apiPedidos.DireccionEnvio.domain.models import DireccionEnvio
from apiPedidos.Usuario.infrastructure.repositories import UsuarioRepository
from apiPedidos.DireccionEnvio.infrastructure.repositories import DireccionEnvioRepositorio
from apiPedidos.Pedido.infrastructure.repositories import PedidoRepository  
from apiPedidos.Pedido.dtos.Pedido_dto import Pedidodto
from apiPedidos.Pedido.dtos.updatePedidodto import UpdatePedidodto
from apiPedidos.Pedido.domain.models import EstadoPedido
class PedidoService:

    @staticmethod
    def createPedido(pedido_data):
        usuario = UsuarioRepository.getUsuarioById(pedido_data['usuario'])
        if not usuario:
            raise UsuarioNotFoundPedido("El usuario no existe")
        print("Usuario encontrado", usuario)
        direccion = DireccionEnvioRepositorio.getDireccionById(pedido_data['direccion'])
       
        print("Direccion encontrada", direccion)
        if not direccion:
            raise DireccionNotFoundPedido("La dirección no existe")
        fecha_entrega = datetime.now() + timedelta(days=3)
        pedido = Pedido(
            usuario=usuario,
            direccion=direccion,
            fechaEntrega = fecha_entrega,
            total=pedido_data['total'],
            observaciones=pedido_data.get('observaciones', '')
        )
        PedidoRepository.savePedido(pedido)
    @staticmethod
    def getPedidoById(pedidoId):
        pedido = PedidoRepository.getPedidoById(pedidoId)
        if not pedido:
            raise PedidoNotFound("El pedido no existe")
        return Pedidodto(
            id_pedido=pedido.pedidoId,
            id_cliente=pedido.usuario.idUsuario,
            id_direccion=pedido.direccion.direccionId,
            fecha_pedido=pedido.fechaPedido,
            fecha_entrega=pedido.fechaEntrega,
            estado_pedido=pedido.estado,
            total_pedido=pedido.total,
            observaciones=pedido.observaciones
        )
    @staticmethod
    def getPedidosByUserId(userid):
        usuario = UsuarioRepository.getUsuarioById(userid)
        if not usuario:
            raise UsuarioNotFoundPedido("El usuario no existe")
        direccion = DireccionEnvioRepositorio.getDireccionById(userid)
        if not direccion:
            raise DireccionNotFoundPedido("La dirección no existe")
        pedidos = PedidoRepository.getPedidosByUserId(userid)
        return [Pedidodto(
            id_pedido=pedido.pedidoId,
            id_cliente=pedido.usuario.idUsuario,
            id_direccion=direccion.direccionId,
            fecha_pedido=pedido.fechaPedido,
            fecha_entrega=pedido.fechaEntrega,
            estado_pedido=pedido.estado,
            total_pedido=pedido.total,
            observaciones=pedido.observaciones
        ) for pedido in pedidos]
    
    @staticmethod
    def getPedidoByUserIdAndPedidoId(userid, pedidoId):
        usuario = UsuarioRepository.getUsuarioById(userid)
        if not usuario:
            raise UsuarioNotFoundPedido("El usuario no existe")
        direccion = DireccionEnvioRepositorio.getDireccionById(userid)
        if not direccion:
            raise DireccionNotFoundPedido("La dirección no existe")
        pedido = PedidoRepository.getPedidoByUserIdAndPedidoId(userid, pedidoId)
        if not pedido:
            raise PedidoNotFound("El pedido no existe")
        return Pedidodto(
            id_pedido=pedido.pedidoId,
            id_cliente=pedido.usuario.idUsuario,
            id_direccion=direccion.direccionId,
            fecha_pedido=pedido.fechaPedido,
            fecha_entrega=pedido.fechaEntrega,
            estado_pedido=pedido.estado,
            total_pedido=pedido.total,
            observaciones=pedido.observaciones
        )

    @staticmethod
    def getPeidosByUserIdAndEstado(userid, estado):
        usuario = UsuarioRepository.getUsuarioById(userid)
        if not usuario:
            raise UsuarioNotFoundPedido("El usuario no existe")
        direccion = DireccionEnvioRepositorio.getDireccionById(userid)
        if not direccion:
            raise DireccionNotFoundPedido("La dirección no existe")
        pedidos = PedidoRepository.getPeidosByUserIdAndEstado(userid, estado)
        return [Pedidodto(
            id_pedido=pedido.pedidoId,
            id_cliente=pedido.usuario.idUsuario,
            id_direccion=direccion.direccionId,
            fecha_pedido=pedido.fechaPedido,
            fecha_entrega=pedido.fechaEntrega,
            estado_pedido=pedido.estado,
            total_pedido=pedido.total,
            observaciones=pedido.observaciones
        ) for pedido in pedidos]
    @staticmethod
    def getPedidoByUserIdAndFechaPedido(idUsuario, fechaPedidodesde, fechaPedidoHasta):
        usuario = UsuarioRepository.getUsuarioById(idUsuario)
        if not usuario:
            raise UsuarioNotFoundPedido("El usuario no existe")
        pedidos = PedidoRepository.getPedidoByUserIdAndFechaPedido(idUsuario, fechaPedidodesde, fechaPedidoHasta)
        return [Pedidodto(
            id_pedido=pedido.pedidoId,
            id_cliente=pedido.usuario.idUsuario,
            id_direccion=pedido.direccion.direccionId,
            fecha_pedido=pedido.fechaPedido,
            fecha_entrega=pedido.fechaEntrega,
            estado_pedido=pedido.estado,
            total_pedido=pedido.total,
            observaciones=pedido.observaciones
        ) for pedido in pedidos]
    @staticmethod
    def getPedidosByEstado(estado):
        pedidos = PedidoRepository.getPedidosByEstado(estado)
        return [Pedidodto(
            id_pedido=pedido.pedidoId,
            id_cliente=pedido.usuario.idUsuario,
            id_direccion=pedido.direccion.direccionId,
            fecha_pedido=pedido.fechaPedido,
            fecha_entrega=pedido.fechaEntrega,
            estado_pedido=pedido.estado,
            total_pedido=pedido.total,
            observaciones=pedido.observaciones
        ) for pedido in pedidos]
    
    @staticmethod
    def getPedidosByRangeFechaPedido(fechadesde, fechahasta):
        pedidos = PedidoRepository.getPedidosByRangeFechaPedido(fechadesde, fechahasta)
        return [Pedidodto(
            id_pedido=pedido.pedidoId,
            id_cliente=pedido.usuario.idUsuario,
            id_direccion=pedido.direccion.direccionId,
            fecha_pedido=pedido.fechaPedido,
            fecha_entrega=pedido.fechaEntrega,
            estado_pedido=pedido.estado,
            total_pedido=pedido.total,
            observaciones=pedido.observaciones
        ) for pedido in pedidos]
    
    @staticmethod
    def EditarPedido(pedidoId, pedido_dto):
        pedido = PedidoRepository.getPedidoById(pedidoId)
        if not pedido:
            raise PedidoNotFound("El pedido no existe")
        if pedido_dto.fecha_entrega:
            pedido.estado = pedido_dto.fecha_entrega
        if pedido_dto.estado_pedido:
            if pedido_dto.estado_pedido not in EstadoPedido:
                raise InvalidPedidoException("Estado de pedido no válido")
            pedido.estado = pedido_dto.estado_pedido
        if pedido_dto.total_pedido:
            pedido.total = pedido_dto.total_pedido
        if pedido_dto.observaciones:
            pedido.observaciones = pedido_dto.observaciones
        PedidoRepository.savePedido(pedido)
    
    @staticmethod
    def deletePedido(pedidoId):
        pedido = PedidoRepository.getPedidoById(pedidoId)
        if not pedido:
            raise PedidoNotFound("El pedido no existe")
        PedidoRepository.deletePedido(pedidoId)