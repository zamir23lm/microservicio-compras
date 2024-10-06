from apiPedidos.Usuario.domain.models import Usuario
from apiPedidos.Usuario.exceptions.Usuario_exceptions import UsuarioException, EmailAlreadyRegisteredException, InvalidPhoneNumberException
from apiPedidos.Usuario.infrastructure.repositories import UsuarioRepository
from apiPedidos.Usuario.dtos.Usuario_dto import UsuarioDto
from apiPedidos.Usuario.dtos.id_usuario_dto import idUsuarioDto

class UsuarioService:
    @staticmethod
    def createUsuario(nombre, apellido, email, telefono):
        try:
            UsuarioRepository.verificarEmailUnico(email)
            if not telefono.isdigit() or len(telefono) >11:
                raise InvalidPhoneNumberException("El número de teléfono es inválido")
            usuario = Usuario(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono
            )
            UsuarioRepository.guardarUsuario(usuario)
            return UsuarioDto(usuario.idUsuario, usuario.nombre, usuario.apellido, usuario.email, usuario.telefono)
        except (EmailAlreadyRegisteredException) as e:
            raise UsuarioException(str(e))
        
    @staticmethod
    def get_user_email(email):  
        usuario = UsuarioRepository.get_user_by_email(email)
        if not usuario:
            raise UsuarioException("El usuario no existe con el email " + str(email))
        return UsuarioDto(usuario.idUsuario, usuario.nombre, usuario.apellido, usuario.email, usuario.telefono)
    
    @staticmethod
    def get_user_by_id(idUsuario):
        usuario = UsuarioRepository.get_user_by_id(idUsuario)
        if not usuario:
            raise UsuarioException("El usuario no existe con el id " + str(idUsuario))
        return UsuarioDto(usuario.idUsuario, usuario.nombre, usuario.apellido, usuario.email, usuario.telefono)
    
    @staticmethod
    def get_user_id(idUsuario):
        usuario = UsuarioRepository.getUsuarioById(idUsuario)
        if not usuario:
            raise UsuarioException("El usuario no existe con el id " + str(idUsuario))
        return idUsuarioDto(usuario.idUsuario)
    
    @staticmethod
    def login_usuario(email):
        usuario = UsuarioRepository.get_user_by_email(email)
        if not usuario:
            raise UsuarioException("El usuario no existe con el email " + str(email))
        return UsuarioDto(usuario.idUsuario, usuario.nombre, usuario.apellido, usuario.email, usuario.telefono)
    
    @staticmethod
    def deleteUsuario(idUsuario):
        usuario = UsuarioRepository.get_user_by_id(idUsuario)
        if not usuario:
            raise UsuarioException("El usuario no existe con el id " + str(idUsuario))
        UsuarioRepository.delete_user(idUsuario)
        print("Usuario eliminado")
        return None
    
    @staticmethod
    def update_email(idUsuario, email):
        usuario = UsuarioRepository.get_user_by_id(idUsuario)
        if not usuario:
            raise UsuarioException("El usuario no existe con el id " + str(idUsuario))
        UsuarioRepository.update_email(idUsuario, email)
        print("Email actualizado")
        return None
    
    @staticmethod
    def update_telefono(idUsuario, telefono):
        usuario = UsuarioRepository.get_user_by_id(idUsuario)
        if not usuario:
            raise UsuarioException("El usuario no existe con el id " + str(idUsuario))
        if not telefono.isdigit() or len(telefono) > 11:
            raise InvalidPhoneNumberException("El número de teléfono es inválido")
        UsuarioRepository.update_telefono(idUsuario, telefono)
        print("Telefono actualizado")
        return None
    
    @staticmethod
    def update_all_usuario(usuario_dto: UsuarioDto):
        usuario = UsuarioRepository.get_user_by_id(usuario_dto.idUsuario)
        if not usuario:
            raise UsuarioException("El usuario no existe con el id " + str(usuario_dto.idUsuario))
        if not usuario_dto.telefono.isdigit() or len(usuario_dto.telefono) >11:
            raise InvalidPhoneNumberException("El número de teléfono es inválido")
        usuario.nombre = usuario_dto.nombre
        usuario.apellido = usuario_dto.apellido
        usuario.email = usuario_dto.email
        usuario.telefono = usuario_dto.telefono
        UsuarioRepository.guardarUsuario(usuario)
        print("Usuario actualizado")
        return None
