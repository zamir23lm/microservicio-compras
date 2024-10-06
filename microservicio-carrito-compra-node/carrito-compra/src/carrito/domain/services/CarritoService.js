const CarritoRepository = require('../../infrastructure/CarritoRepository');


class CarritoService{
    async createCarrito(carrito){
        return await CarritoRepository.createCarrito(carrito);
    }
    async obtenerTodosLosCarritos(){
        return await CarritoRepository.obtenerTodosLosCarritos();
    }
    async obtenerCarritoPorId(id){
        return await CarritoRepository.obtenerCarritoPorId(id);
    }
    async obtenerCarritosPorUsuario(usuarioId){
        return await CarritoRepository.obtenerCarritosPorUsuario(usuarioId);
    }
    async modificarCarritoPagado(id){
        return await CarritoRepository.modificarCarritoPagado(id);
    }
    async eliminarCarrito(id){
        return await CarritoRepository.eliminarCarrito(id);
    }
    async editarDetalleCarrito(id, detalleCarritoId){
        return await CarritoRepository.editarDetalleCarrito(id, detalleCarritoId);
    }

}
module.exports = new CarritoService();