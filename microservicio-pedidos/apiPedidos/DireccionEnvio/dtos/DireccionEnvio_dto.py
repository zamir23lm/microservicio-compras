class DireccionEnvioDto:
    def __init__(self, id, usuarioId, direccion, distrito, provincia, departamento, pais, codigoPostal, instrucciones, latitud, longitud):
        self.id = id
        self.usuarioId = usuarioId
        self.direccion = direccion
        self.distrito = distrito
        self.provincia = provincia
        self.departamento = departamento
        self.pais = pais
        self.codigoPostal = codigoPostal
        self.instrucciones = instrucciones
        self.latitud = latitud
        self.longitud = longitud

    def __repr__(self):
        return f"DireccionEnvioDto(id={self.id}, usuarioId={self.usuarioId}, direccion={self.direccion}, distrito={self.distrito}, provincia={self.provincia}, departamento={self.departamento}, pais={self.pais}, codigoPostal={self.codigoPostal}, instrucciones={self.instrucciones}, latitud={self.latitud}, longitud={self.longitud})"
