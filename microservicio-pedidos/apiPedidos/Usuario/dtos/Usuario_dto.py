class UsuarioDto:
    def __init__(self, idUsuario, nombre, apellido, email, telefono):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __repr__(self):
        return f"UsuarioDto(idUsuario={self.idUsuario}, nombre={self.nombre}, apellido={self.apellido}, email={self.email}, telefono={self.telefono})"