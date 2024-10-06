from apiPedidos.Usuario.domain.models import Usuario
from apiPedidos.Usuario.exceptions.Usuario_exceptions import EmailAlreadyRegisteredException
class UsuarioRepository:
    @staticmethod
    def getUsuarioByEmail(email):
        try:
            return Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return None
        
    @staticmethod
    def getUsuarioById(idUsuario):
        try:
            return Usuario.objects.get(idUsuario=idUsuario)
        except Usuario.DoesNotExist:
            return None
        
    @staticmethod
    def guardarUsuario(usuario):
        usuario.save()

    @staticmethod
    def verificarEmailUnico(email):
        if Usuario.objects.filter(email=email).exists():
            raise EmailAlreadyRegisteredException("El email ya esta registrado")
        
    @staticmethod
    def get_user_by_email(email):
        try:
            return Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return None
        
    @staticmethod
    def get_user_by_id(idUsuario):
        try:
            return Usuario.objects.get(idUsuario=idUsuario)
        except Usuario.DoesNotExist:
            return None
        
    @staticmethod
    def get_all_users():
        try:
            return Usuario.objects.all()
        except Usuario.DoesNotExist:
            return None
    
    @staticmethod
    def delete_user(idUsuario):
        try:
            Usuario.objects.get(idUsuario=idUsuario).delete()
        except Usuario.DoesNotExist:
            return None
    
    @staticmethod
    def update_email(idUsuario, email):
        try:
            usuario = Usuario.objects.get(idUsuario=idUsuario)
            usuario.email = email
            usuario.save()
        except Usuario.DoesNotExist:
            return None
   
        
    @staticmethod
    def update_telefono(idUsuario, telefono):
        try:
            usuario = Usuario.objects.get(idUsuario=idUsuario)
            usuario.telefono = telefono
            usuario.save()
        except Usuario.DoesNotExist:
            return None