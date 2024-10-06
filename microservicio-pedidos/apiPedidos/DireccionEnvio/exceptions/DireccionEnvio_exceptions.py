

class DIreccionException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message

class DireccionNotFound(DIreccionException):
    pass

class InvalidDireccionException(DIreccionException):
    pass

class UsuarioNotFoundDireccion(DIreccionException):
    pass