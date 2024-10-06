from rest_framework import serializers
from apiPedidos.DireccionEnvio.domain.models import DireccionEnvio
from apiPedidos.Usuario.domain.models import Usuario
from apiPedidos.Usuario.infrastructure.repositories import UsuarioRepository
from apiPedidos.DireccionEnvio.exceptions.DireccionEnvio_exceptions import DireccionNotFound, InvalidDireccionException, UsuarioNotFoundDireccion
from apiPedidos.DireccionEnvio.infrastructure.repositories import DireccionEnvioRepositorio
from apiPedidos.DireccionEnvio.dtos.DireccionEnvio_dto import DireccionEnvioDto
from apiPedidos.DireccionEnvio.dtos.direcciondto import Direcciondto


class DireccionEnvioService:
    @staticmethod
    def createDireccionEnvio(direccion_data):
        print("Datos recibidos", direccion_data)
        usuario = UsuarioRepository.getUsuarioById(direccion_data['usuario'])
        if not usuario:
            raise UsuarioNotFoundDireccion("El usuario no existe")
        print("Usuario encontrado", usuario)
        direccion = DireccionEnvio(
            usuario=usuario, 
            direccion=direccion_data['direccion'],
            distrito=direccion_data.get('distrito', ''),  
            provincia=direccion_data.get('provincia', ''),
            departamento=direccion_data['departamento'],
            pais=direccion_data['pais'],
            codigoPostal=direccion_data.get('codigoPostal', ''),
            instrucciones=direccion_data.get('instrucciones', ''),
            latitud=direccion_data['latitud'],
            longitud=direccion_data['longitud']
        )

        DireccionEnvioRepositorio.saveDireccionEnvio(direccion)
        print("Direccion guardada", direccion)
        return DireccionEnvioDto(
            direccion.direccionId,
            usuario.idUsuario, 
            direccion.direccion,
            direccion.distrito,
            direccion.provincia,
            direccion.departamento,
            direccion.pais,
            direccion.codigoPostal,
            direccion.instrucciones,
            direccion.latitud,
            direccion.longitud
        )


    @staticmethod
    def get_direccionById(direccionId):
        direccion = DireccionEnvioRepositorio.getDireccionById(direccionId)
        if not direccion:
            raise DireccionNotFound("La dirección no existe")
        print("Direccion encontrada", direccion)
        return Direcciondto(direccion.direccionId,
                                  direccion.usuario.idUsuario, 
                                  direccion.direccion,
                                    direccion.distrito, 
                                    direccion.provincia, 
                                    direccion.departamento, 
                                    direccion.pais, 
                                    direccion.codigoPostal, 
                                    direccion.instrucciones, 
                                    direccion.latitud, 
                                    direccion.longitud)
    
    @staticmethod
    def get_direccionesByUserId(idUsuario):
        usuario = UsuarioRepository.getUsuarioById(idUsuario)
        print("Usuario encontrado", usuario)
        if not usuario:
            raise UsuarioNotFoundDireccion("El usuario no existe")
        direcciones = DireccionEnvioRepositorio.getDireccionByUserId(idUsuario)
        print("Direcciones encontradas", direcciones)
        if not direcciones:
            raise UsuarioNotFoundDireccion("El usuario no tiene direcciones")
        direcciones_dto = [Direcciondto(
            direccion.direccionId,
            direccion.usuario.idUsuario,
            direccion.direccion,
            direccion.distrito,
            direccion.provincia,
            direccion.departamento,
            direccion.pais,
            direccion.codigoPostal,
            direccion.instrucciones,
            direccion.latitud,
            direccion.longitud
        ) for direccion in direcciones]
        print("Direcciones encontradas", direcciones_dto)
        return direcciones_dto
    
    @staticmethod
    def deleteDireccion(direccionId):
        direccion = DireccionEnvioRepositorio.getDireccionById(direccionId)
        if not direccion:
            raise DireccionNotFound("La dirección no existe")
        DireccionEnvioRepositorio.deleteDireccion(direccionId)
        return None

    @staticmethod
    def EditarDireccion(direccionId, usuarioId, DireccionDto):

        direccion = DireccionEnvioRepositorio.getDireccionById(direccionId)
        if not direccion:
            raise DireccionNotFound("La dirección no existe")
        usuario = UsuarioRepository.getUsuarioById(usuarioId)
        if not usuario:
            raise UsuarioNotFoundDireccion("El usuario no existe")
        if(usuarioId != direccion.usuario.idUsuario):
            raise InvalidDireccionException("El usuario no coincide")
        if(DireccionDto.direccion!=""):
            direccion.direccion = DireccionDto.direccion
        if(DireccionDto.distrito!=""):
            direccion.distrito = DireccionDto.distrito
        if(DireccionDto.provincia!=""):
            direccion.provincia = DireccionDto.provincia
        if(DireccionDto.departamento!=""):
            direccion.departamento = DireccionDto.departamento
        if(DireccionDto.pais!=""):
            direccion.pais = DireccionDto.pais
        if(DireccionDto.codigoPostal!=""):
            direccion.codigoPostal = DireccionDto.codigoPostal
        if(DireccionDto.instrucciones!=""):
            direccion.instrucciones = DireccionDto.instrucciones
        if(DireccionDto.latitud!=""):
            direccion.latitud = DireccionDto.latitud
        if(DireccionDto.longitud!=""):
            direccion.longitud = DireccionDto.longitud
        DireccionEnvioRepositorio.saveDireccionEnvio(direccion)
        return DireccionEnvioDto(direccion.direccionId, direccion.usuario.idUsuario, direccion.direccion, direccion.distrito, direccion.provincia, direccion.departamento, direccion.pais, direccion.codigoPostal, direccion.instrucciones, direccion.latitud, direccion.longitud)