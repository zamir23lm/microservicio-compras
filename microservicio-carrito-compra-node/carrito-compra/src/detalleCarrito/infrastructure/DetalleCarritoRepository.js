const DetalleCarrito = require('../domain/models/DetalleCarrito');

class DetalleCarritoRepository{
    async crearDetalleCarrito(detalleCarritoData){
        const detalleCarrito = new DetalleCarrito(detalleCarritoData);
        detalleCarrito.calcularTotal();
        return await detalleCarrito.save();
    }
    async obtenerTodosLosDetallesCarrito(){
        return await DetalleCarrito.find();
    }
    async obtenerDetalleCarritoPorId(id){
        return await DetalleCarrito.findById(id).exec();
    }
    async eliminarDetalleCarrito(id){
        return await DetalleCarrito.findByIdAndDelete(id);
    }

}
module.exports = new DetalleCarritoRepository();