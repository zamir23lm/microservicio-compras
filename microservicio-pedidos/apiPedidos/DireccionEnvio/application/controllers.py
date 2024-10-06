from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apiPedidos.DireccionEnvio.domain.services import DireccionEnvioService
from apiPedidos.DireccionEnvio.serializers import DireccionEnvioSerializer, EditDIreccionSerializer, DirecciondtoSerializer, UpdateDireccionSerializer
from apiPedidos.DireccionEnvio.dtos.direcciondto import Direcciondto
from apiPedidos.DireccionEnvio.dtos.updatedireccion import UpdateDirecciondto
from apiPedidos.DireccionEnvio.exceptions.DireccionEnvio_exceptions import DireccionNotFound, UsuarioNotFoundDireccion
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class DireccionEnvioGuardar(APIView):
    """
    Guardar una nueva dirección de envío
    """

    @swagger_auto_schema(
        operation_description="Crea una nueva dirección de envío",
        request_body=DireccionEnvioSerializer,
        responses={
            201: 'Dirección creada correctamente',
            400: 'Error en la solicitud'
        }
    )
    def post(self, request):
        serializer = DireccionEnvioSerializer(data=request.data)
        if serializer.is_valid():
            try:
                direccion = DireccionEnvioService.createDireccionEnvio(
                    direccion_data=serializer.data
                )
                return Response({
                    'message': 'Dirección creada correctamente',
                    "Direccion": serializer.data
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Formulario para registrar una dirección de envío",
        responses={200: 'Formulario de creación de dirección'}
    )
    def get(self, request):
        return Response({
            'message': 'Para registrar una dirección, usa el método POST con los siguientes campos:',
            'fields': DireccionEnvioSerializer().data
        }, status=status.HTTP_200_OK)

class DireccionEnvioDetalles(APIView):
    """
    Obtener detalles de una dirección de envío por ID
    """

    @swagger_auto_schema(
        operation_description="Obtiene los detalles de una dirección por ID",
        responses={
            200: DirecciondtoSerializer,
            400: 'Error en la solicitud',
            404: 'Dirección no encontrada'
        }
    )
    def get(self, request, *args, **kwargs):
        direccionId = kwargs.get('direccionId')
        try:
            direccion = DireccionEnvioService.get_direccionById(direccionId)
            serializer = DirecciondtoSerializer(direccion)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DireccionNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DireccioEnvioByUser(APIView):
    """
    Obtener direcciones de un usuario por ID
    """

    @swagger_auto_schema(
        operation_description="Obtiene todas las direcciones de un usuario por ID",
        responses={
            200: DirecciondtoSerializer(many=True),
            400: 'Error en la solicitud'
        }
    )
    def get(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')
        if not idUsuario:
            return Response({"error": "idUsuario es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            direcciones = DireccionEnvioService.get_direccionesByUserId(idUsuario)
            serializer = DirecciondtoSerializer(direcciones, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DireccionEnvioDelete(APIView):
    """
    Eliminar una dirección de envío
    """

    @swagger_auto_schema(
        operation_description="Elimina una dirección de envío por ID",
        responses={
            200: 'Dirección eliminada correctamente',
            400: 'Error en la solicitud'
        }
    )
    def delete(self, request, *args, **kwargs):
        direccionId = kwargs.get('direccionId')
        try:
            DireccionEnvioService.deleteDireccion(direccionId)
            return Response({
                'message': 'Dirección eliminada correctamente',
            }, status=status.HTTP_200_OK)
        except DireccionNotFound as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DireccionEnvioEditar(APIView):
    """
    Editar una dirección de envío
    """

    @swagger_auto_schema(
        operation_description="Edita una dirección de envío por ID",
        request_body=UpdateDireccionSerializer,
        responses={
            200: 'Dirección actualizada correctamente',
            400: 'Error en la solicitud',
            404: 'Dirección o usuario no encontrados'
        }
    )
    def put(self, request, *args, **kwargs):
        direccionId = kwargs.get('direccionId')
        usuarioId = kwargs.get('usuarioId')
        serializer = UpdateDireccionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                direccion_dto = UpdateDirecciondto(
                    direccion=serializer.validated_data['direccion'],
                    distrito=serializer.validated_data['distrito'],
                    provincia=serializer.validated_data['provincia'],
                    departamento=serializer.validated_data['departamento'],
                    pais=serializer.validated_data['pais'],
                    codigoPostal=serializer.validated_data['codigoPostal'],
                    instrucciones=serializer.validated_data['instrucciones'],
                    latitud=serializer.validated_data['latitud'],
                    longitud=serializer.validated_data['longitud']
                )
                DireccionEnvioService.EditarDireccion(direccionId, usuarioId, direccion_dto)
                return Response(
                    {
                        'message': 'Dirección actualizada correctamente',
                    }, status=status.HTTP_200_OK
                )
            except DireccionNotFound as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
            except UsuarioNotFoundDireccion as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
