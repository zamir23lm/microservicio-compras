from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apiPedidos.Pedido.domain.services import PedidoService
from apiPedidos.Pedido.serializers import PedidoSerializer, EditPedidoSerializer, PedidoDtoSerializer
from apiPedidos.Pedido.dtos.Pedido_dto import Pedidodto
from apiPedidos.Pedido.exceptions.Pedido_exceptions import PedidoNotFound, InvalidPedidoException, UsuarioNotFoundPedido, DireccionNotFoundPedido
from apiPedidos.Pedido.dtos.updatePedidodto import UpdatePedidodto
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class PedidoGuardar(APIView):
    """
    Guardar un nuevo pedido
    """

    @swagger_auto_schema(
        operation_description="Crea un nuevo pedido",
        request_body=PedidoSerializer,
        responses={
            201: 'Pedido creado correctamente',
            400: 'Error en la solicitud'
        }
    )
    def post(self, request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                pedido = PedidoService.createPedido(
                    pedido_data=serializer.data
                )
                return Response({
                    'message': 'Pedido creado correctamente',
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetallesPedidoId(APIView):
    """
    Obtener detalles del pedido por ID
    """

    @swagger_auto_schema(
        operation_description="Obtiene los detalles de un pedido por ID",
        responses={
            200: PedidoDtoSerializer,
            404: 'Pedido no encontrado',
            400: 'Error en la solicitud'
        }
    )
    def get(self, request, *args, **kwargs):
        pedidoId = kwargs.get('pedidoId')
        try:
            pedido = PedidoService.getPedidoById(pedidoId)
            serializer = PedidoDtoSerializer(pedido)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PedidoByUserId(APIView):
    """
    Obtener pedidos por ID de usuario
    """

    @swagger_auto_schema(
        operation_description="Obtiene todos los pedidos de un usuario",
        responses={
            200: PedidoDtoSerializer(many=True),
            404: 'Pedidos no encontrados',
            400: 'Error en la solicitud'
        }
    )
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        try:
            pedidos = PedidoService.getPedidosByUserId(userId)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PedidoByUserIdAndPedidoId(APIView):
    """
    Obtener pedido por ID de usuario y pedido
    """

    @swagger_auto_schema(
        operation_description="Obtiene un pedido por el ID del usuario y del pedido",
        responses={
            200: PedidoDtoSerializer,
            404: 'Pedido no encontrado',
            400: 'Error en la solicitud'
        }
    )
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        pedidoId = kwargs.get('pedidoId')
        try:
            pedido = PedidoService.getPedidoByUserIdAndPedidoId(userId, pedidoId)
            serializer = PedidoDtoSerializer(pedido)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PedidoByUserIdAndEstado(APIView):
    """
    Obtener pedidos de un usuario por estado
    """

    @swagger_auto_schema(
        operation_description="Obtiene los pedidos de un usuario filtrados por estado",
        manual_parameters=[
            openapi.Parameter('estado', openapi.IN_QUERY, description="Estado del pedido", type=openapi.TYPE_STRING)
        ],
        responses={
            200: PedidoDtoSerializer(many=True),
            404: 'Pedidos no encontrados',
            400: 'Error en la solicitud'
        }
    )
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        estado = request.query_params.get('estado')
        try:
            pedidos = PedidoService.getPeidosByUserIdAndEstado(userId, estado)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PedidoByUserIdAndFechaPedido(APIView):
    """
    Obtener pedidos por usuario y rango de fechas
    """

    @swagger_auto_schema(
        operation_description="Obtiene los pedidos de un usuario en un rango de fechas",
        manual_parameters=[
            openapi.Parameter('fechaPedidodesde', openapi.IN_QUERY, description="Fecha de inicio", type=openapi.TYPE_STRING),
            openapi.Parameter('fechaPedidoHasta', openapi.IN_QUERY, description="Fecha de fin", type=openapi.TYPE_STRING)
        ],
        responses={
            200: PedidoDtoSerializer(many=True),
            404: 'Pedidos no encontrados',
            400: 'Error en la solicitud'
        }
    )
    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId')
        fechaPedidodesde = request.query_params.get('fechaPedidodesde')
        fechaPedidoHasta = request.query_params.get('fechaPedidoHasta')
        try:
            pedidos = PedidoService.getPedidoByUserIdAndFechaPedido(userId, fechaPedidodesde, fechaPedidoHasta)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PedidosByEstado(APIView):
    """
    Obtener pedidos por estado
    """

    @swagger_auto_schema(
        operation_description="Obtiene pedidos filtrados por estado",
        manual_parameters=[
            openapi.Parameter('estado', openapi.IN_QUERY, description="Estado del pedido", type=openapi.TYPE_STRING)
        ],
        responses={
            200: PedidoDtoSerializer(many=True),
            404: 'Pedidos no encontrados',
            400: 'Error en la solicitud'
        }
    )
    def get(self, request, *args, **kwargs):
        estado = request.query_params.get('estado')
        try:
            pedidos = PedidoService.getPedidosByEstado(estado)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PedidosByRangeFechaPedido(APIView):
    """
    Obtener pedidos por rango de fechas
    """

    @swagger_auto_schema(
        operation_description="Obtiene pedidos en un rango de fechas",
        manual_parameters=[
            openapi.Parameter('fechaPedidodesde', openapi.IN_QUERY, description="Fecha de inicio", type=openapi.TYPE_STRING),
            openapi.Parameter('fechaPedidoHasta', openapi.IN_QUERY, description="Fecha de fin", type=openapi.TYPE_STRING)
        ],
        responses={
            200: PedidoDtoSerializer(many=True),
            404: 'Pedidos no encontrados',
            400: 'Error en la solicitud'
        }
    )
    def get(self, request, *args, **kwargs):
        fechaPedidodesde = request.query_params.get('fechaPedidodesde')
        fechaPedidoHasta = request.query_params.get('fechaPedidoHasta')
        try:
            pedidos = PedidoService.getPedidosByRangeFechaPedido(fechaPedidodesde, fechaPedidoHasta)
            serializer = PedidoDtoSerializer(pedidos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PedidoNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PedidoEditar(APIView):
    """
    Editar un pedido
    """

    @swagger_auto_schema(
        operation_description="Edita un pedido por ID",
        request_body=EditPedidoSerializer,
        responses={
            200: 'Pedido actualizado correctamente',
            400: 'Error en la solicitud',
            404: 'Pedido no encontrado'
        }
    )
    def put(self, request, *args, **kwargs):
        pedidoId = kwargs.get('pedidoId')
        serializer = EditPedidoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                pedido_dto = UpdatePedidodto(
                    fecha_entrega=serializer.validated_data['fechaEntrega'],   
                    estado_pedido=serializer.validated_data['estado'],
                    total_pedido=serializer.validated_data['total'],
                    observaciones=serializer.validated_data['observaciones']
                )
                PedidoService.EditarPedido(pedidoId, pedido_dto)
                return Response(
                    {
                        'message': 'Pedido actualizado correctamente',
                    }, status=status.HTTP_200_OK
                )
            except PedidoNotFound as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
            except InvalidPedidoException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PedidoDelete(APIView):
    """
    Eliminar un pedido
    """

    @swagger_auto_schema(
        operation_description="Elimina un pedido por ID",
        responses={
            200: 'Pedido eliminado correctamente',
            400: 'Error en la solicitud'
        }
    )
    def delete(self, request, *args, **kwargs):
        pedidoId = kwargs.get('pedidoId')
        try:
            PedidoService.deletePedido(pedidoId)
            return Response({
                'message': 'Pedido eliminado correctamente',
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
