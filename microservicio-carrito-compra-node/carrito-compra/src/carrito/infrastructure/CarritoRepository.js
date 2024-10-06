const Carrito = require('../domain/models/Carrito');

class CarritoRepository{
    async createCarrito(carritoData){
        const carrito = new Carrito(carritoData);
        console.log(carrito, "carrito");
        return await carrito.save();    
    }
    async obtenerTodosLosCarritos(){
        return await Carrito.find();
    }
    async obtenerCarritoPorId(id){
        return await Carrito.findById(id);
    }
    async obtenerCarritosPorUsuario(usuarioId){
        return await Carrito.find({usuario_id: usuarioId});
    }
    async modificarCarritoPagado(id){
        return await Carrito.findByIdAndUpdate(id, 
            {estado: 'pagado'}, 
            {new: true});
    }
    async eliminarCarrito(id){
        return await Carrito.findByIdAndDelete(id);
    }
    async editarDetalleCarrito(id, detalleCarritoId){
        return await Carrito.findByIdAndUpdate(id,
            {carritoDetalle_id: detalleCarritoId},
            {new: true});
        
    }

}
module.exports = new CarritoRepository();