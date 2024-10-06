class Pedidodto:
    def __init__(self, id_pedido, id_cliente,id_direccion, fecha_pedido, fecha_entrega,estado_pedido, total_pedido, observaciones):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.id_direccion = id_direccion
        self.fecha_pedido = fecha_pedido
        self.fecha_entrega = fecha_entrega
        self.estado_pedido = estado_pedido
        self.total_pedido = total_pedido
        self.observaciones = observaciones
