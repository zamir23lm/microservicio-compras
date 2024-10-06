const DetallesCarritoRepository = require('../../infrastructure/DetalleCarritoRepository');

class DetalleCarritoService{
    async crearDetalleCarrito(detalleCarrito){
        const detallesCarrito = await DetallesCarritoRepository.crearDetalleCarrito(detalleCarrito);
        return detallesCarrito;
    }
    //Agregar producto a detalle carrito
    async agregarProducto(detalleCarritoId, producto){
        const detalleCarrito = await DetallesCarritoRepository.obtenerDetalleCarritoPorId(detalleCarritoId);
        if(!detalleCarrito){
            throw new Error('Detalle de carrito no encontrado');
        }
        if(!detalleCarrito.productos){
            detalleCarrito.productos = [];
        }
        detalleCarrito.productos.push(producto);
        detalleCarrito.calcularTotal();
        return await detalleCarrito.save();
    }
    async obtenerTodosLosDetallesCarrito(){
        return await DetallesCarritoRepository.obtenerTodosLosDetallesCarrito();
    }

    async obtenerDetalleCarritoPorId(id){
        return await DetallesCarritoRepository.obtenerDetalleCarritoPorId(id);
    }
    //Eliminar producto de detalle carrito
    async eliminarProducto(detalleCarritoId, productoId){
        const detalleCarrito = await DetallesCarritoRepository.obtenerDetalleCarritoPorId(detalleCarritoId);
        if(!detalleCarrito){
            throw new Error('Detalle de carrito no encontrado');
        }
        const productosRestantes = detalleCarrito.productos.filter(prod => prod.producto_id != productoId);
        if(productosRestantes.length === detalleCarrito.productos.length){
            throw new Error('Producto no encontrado en detalle de carrito');
        }
        detalleCarrito.productos = productosRestantes;
        detalleCarrito.calcularTotal();
        return await detalleCarrito.save();
    }
    async eliminarDetalleCarrito(id){
        return await DetallesCarritoRepository.eliminarDetalleCarrito(id);
    }

    async editarCantidadProducto(detalleCarritoId, productoId, cantidad){
        const detalleCarrito = await DetallesCarritoRepository.obtenerDetalleCarritoPorId(detalleCarritoId);
        if(!detalleCarrito){
            throw new Error('Detalle de carrito no encontrado');
        }
        const producto = detalleCarrito.productos.find(prod => prod.producto_id == productoId);
        if(!producto){
            throw new Error('Producto no encontrado en detalle de carrito');
        }
        producto.cantidad = cantidad;
        detalleCarrito.calcularTotal();
        return await detalleCarrito.save();
    }
    async obtenerProductoByDetalleCarritoIdAndProductoId(detalleCarritoId, productoId){
        const detalleCarrito = await DetallesCarritoRepository.obtenerDetalleCarritoPorId(detalleCarritoId);
        if(!detalleCarrito){
            throw new Error('Detalle de carrito no encontrado');
        }
        const producto = detalleCarrito.productos.find(prod => prod.producto_id == productoId);
        if(!producto){
            throw new Error('Producto no encontrado en detalle de carrito');
        }
        return producto;
    }
}
module.exports = new DetalleCarritoService();