from apiPedidos.DireccionEnvio.domain.models import DireccionEnvio
from apiPedidos.DireccionEnvio.exceptions.DireccionEnvio_exceptions import DIreccionException, DireccionNotFound, InvalidDireccionException, UsuarioNotFoundDireccion

class DireccionEnvioRepositorio:

    @staticmethod
    def saveDireccionEnvio(direccionEnvio):
        direccionEnvio.save()

    @staticmethod
    def getDireccionById(direccionId):
        try:
            return DireccionEnvio.objects.get(direccionId=direccionId)
        except DireccionEnvio.DoesNotExist:
            return None
        
    @staticmethod
    def getDireccionByUserId(idUsuario):
        try:
            return DireccionEnvio.objects.filter(usuario__idUsuario=idUsuario)
        #Necesitamos devolver las instancias por que estamos inicializando el serializer con un queryset
        except DireccionEnvio.DoesNotExist:
            return None
        
    @staticmethod
    def deleteDireccion(direccionId):
        try:
            DireccionEnvio.objects.get(direccionId=direccionId).delete()
        except DireccionEnvio.DoesNotExist:
            return None
   