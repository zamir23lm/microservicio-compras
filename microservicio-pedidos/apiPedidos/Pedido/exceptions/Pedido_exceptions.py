class PedidoException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message
class PedidoNotFound(PedidoException):
    pass

class InvalidPedidoException(PedidoException):
    pass

class UsuarioNotFoundPedido(PedidoException):
    pass

class DireccionNotFoundPedido(PedidoException):
    pass

class PedidoAlreadyExists(PedidoException):
    pass
