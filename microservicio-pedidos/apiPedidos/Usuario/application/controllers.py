from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apiPedidos.Usuario.domain.services import UsuarioService
from apiPedidos.Usuario.serializers import UsuarioSerializer, UsuarioLoginSerializer, EmailSerializer, TelefonoSerializer
from apiPedidos.Usuario.exceptions.Usuario_exceptions import UsuarioException
from apiPedidos.Usuario.domain.models import Usuario  
from apiPedidos.Usuario.dtos.Usuario_dto import UsuarioDto
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UsuarioRegisterView(APIView):
    """
    Registrar un nuevo usuario
    """

    @swagger_auto_schema(
        operation_description="Registra un nuevo usuario",
        request_body=UsuarioSerializer,
        responses={
            201: openapi.Response('Usuario creado correctamente', UsuarioSerializer),
            400: 'Errores de validación'
        }
    )
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            try:
                usuario = UsuarioService.createUsuario(
                    nombre=serializer.validated_data['nombre'],
                    apellido=serializer.validated_data['apellido'],
                    email=serializer.validated_data['email'],
                    telefono=serializer.validated_data['telefono']
                )
                usuarioCreado = UsuarioSerializer(usuario)
                return Response({
                    'message': 'Usuario creado correctamente',
                    "Usuario": usuarioCreado.data
                }, status=status.HTTP_201_CREATED)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioLoginView(APIView):
    """
    Autenticar un usuario
    """

    @swagger_auto_schema(
        operation_description="Login de usuario",
        request_body=UsuarioLoginSerializer,
        responses={
            200: openapi.Response('Usuario logueado correctamente', UsuarioSerializer),
            400: 'Errores de validación o autenticación'
        }
    )
    def post(self, request):
        serializer = UsuarioLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                usuario = UsuarioService.login_usuario(
                    email=serializer.validated_data['email'],
                )
                serializerInfo = UsuarioSerializer(usuario)
                return Response({
                    'message': 'Usuario logueado correctamente',
                    "Usuario": serializerInfo.data
                    
                }, status=status.HTTP_200_OK)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioDetalles(APIView):
    """
    Obtener detalles del usuario por ID
    """

    @swagger_auto_schema(
        operation_description="Obtiene los detalles de un usuario por su ID",
        responses={
            200: openapi.Response('Detalles del usuario', UsuarioSerializer),
            404: 'Usuario no encontrado'
        }
    )
    def get(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')
        try:
            usuario = UsuarioService.get_user_by_id(idUsuario)
            serializer = UsuarioSerializer(usuario)
            return Response({
                'message': 'Usuario encontrado',
                "Usuario": serializer.data
            }, status=status.HTTP_200_OK)
        except UsuarioException as e:
            return Response({"error usuario no encontrado": str(e)}, status=status.HTTP_404_NOT_FOUND)


class UsuarioDetallesEmail(APIView):
    """
    Obtener detalles del usuario por email
    """

    @swagger_auto_schema(
        operation_description="Obtiene los detalles de un usuario por su email",
        manual_parameters=[
            openapi.Parameter('email', openapi.IN_QUERY, description="Email del usuario", type=openapi.TYPE_STRING)
        ],
        responses={
            200: openapi.Response('Detalles del usuario', UsuarioSerializer),
            400: 'El email es requerido',
            404: 'Usuario no encontrado'
        }
    )
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({
                'error': 'El email es requerido'
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            usuario = UsuarioService.get_user_email(email)
            serializer = UsuarioSerializer(usuario)
            return Response({
                'message': 'Usuario encontrado',
                "Usuario": serializer.data
            }, status=status.HTTP_200_OK)
        except UsuarioException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


class ObtenerId(APIView):
    """
    Obtener ID del usuario
    """

    @swagger_auto_schema(
        operation_description="Obtiene el ID del usuario",
        responses={
            200: openapi.Response('ID del usuario'),
            404: 'Usuario no encontrado'
        }
    )
    def get(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')
        try:
            usuario = UsuarioService.get_user_id(idUsuario)
            return Response({
                'message': 'Usuario encontrado',
                "Usuarioid": usuario.idUsuario,
            }, status=status.HTTP_200_OK)
        except UsuarioException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


class UsuarioDelete(APIView):
    """
    Eliminar un usuario
    """

    @swagger_auto_schema(
        operation_description="Elimina un usuario por su ID",
        responses={
            200: 'Usuario eliminado',
            404: 'Usuario no encontrado'
        }
    )
    def delete(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')
        try:
            UsuarioService.deleteUsuario(idUsuario)
            return Response({
                'message': 'Usuario eliminado'
            }, status=status.HTTP_200_OK)
        except UsuarioException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


class UsuarioUpdateEmail(APIView):
    """
    Actualizar el email del usuario
    """

    @swagger_auto_schema(
        operation_description="Actualiza el email de un usuario",
        request_body=EmailSerializer,
        responses={
            200: 'Email actualizado',
            400: 'Errores de validación'
        }
    )
    def put(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                UsuarioService.update_email(
                    idUsuario=idUsuario,
                    email=serializer.validated_data['email']
                )
                return Response({
                    'message': 'Email actualizado'
                }, status=status.HTTP_200_OK)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class updateTelefono(APIView):
    """
    Actualizar el teléfono del usuario
    """

    @swagger_auto_schema(
        operation_description="Actualiza el teléfono de un usuario",
        request_body=TelefonoSerializer,
        responses={
            200: 'Teléfono actualizado',
            400: 'Errores de validación'
        }
    )
    def put(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')
        serializer = TelefonoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                UsuarioService.update_telefono(
                    idUsuario=idUsuario,
                    telefono=serializer.validated_data['telefono']
                )
                return Response({
                    'message': 'Telefono actualizado'
                }, status=status.HTTP_200_OK)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUsuario(APIView):
    """
    Actualizar toda la información del usuario
    """

    @swagger_auto_schema(
        operation_description="Actualiza todos los datos de un usuario",
        request_body=UsuarioSerializer,
        responses={
            200: 'Usuario actualizado correctamente',
            400: 'Errores de validación o problemas al actualizar',
            404: 'Usuario no encontrado'
        }
    )
    def put(self, request, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')
        try:
            # Verificar si el usuario existe
            usuario = UsuarioService.get_user_by_id(idUsuario)
        except UsuarioException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
        # Serializar los datos recibidos
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Crear un DTO con los datos validados
                usuario_dto = UsuarioDto(
                    idUsuario=idUsuario,
                    nombre=serializer.validated_data['nombre'],
                    apellido=serializer.validated_data['apellido'],
                    email=serializer.validated_data['email'],
                    telefono=serializer.validated_data['telefono']
                )
                # Actualizar el usuario
                UsuarioService.update_all_usuario(usuario_dto)
                return Response({
                    'message': 'Usuario actualizado'
                }, status=status.HTTP_200_OK)
            except UsuarioException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)