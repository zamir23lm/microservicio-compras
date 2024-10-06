require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose'); 
const app = express();
const CarritoController = require('./src/carrito/controllers/CarritoController');
const DetalleCarritoController = require('./src/detalleCarrito/controllers/DetalleCarritoController');
app.use(express.json()); 

// Definir rutas de carrito
app.post('/api/carrito/postear', CarritoController.createCarrito);
app.get('/api/carrito/all', CarritoController.obtenerTodosLosCarritos);
app.get('/api/carrito/:id', CarritoController.obtenerCarritoPorId);
app.get('/api/carrito/usuario/:usuarioId', CarritoController.obtenerCarritosPorUsuario);
app.put('/api/carrito/pagado/:id', CarritoController.modificarCarritoPagado);
app.delete('/api/carrito/:id', CarritoController.eliminarCarrito);
app.put('/api/carrito/detalles/:id', CarritoController.editarDetalleCarrito);
const { swaggerUi, swaggerDocs } = require('./swagger');

//Definir rutas de detalle carrito
app.post('/api/detalleCarrito/postear', DetalleCarritoController.crearDetalleCarrito);
app.put('/api/detalleCarrito/agregarProducto/:id', DetalleCarritoController.agregarProducto);
app.get('/api/detalleCarrito/all', DetalleCarritoController.obtenerTodosLosDetallesCarrito);
app.get('/api/detalleCarrito/:id', DetalleCarritoController.obtenerDetalleCarritoPorId);
app.delete('/api/detalleCarrito/:id', DetalleCarritoController.eliminarDetalleCarrito);
app.delete('/api/detalleCarrito/:id/:productoid', DetalleCarritoController.eliminarProducto);
app.put('/api/detalleCarrito/:id/:productoid', DetalleCarritoController.editarCantidadProducto);
app.get('/api/detalleCarrito/:id/:productoid', DetalleCarritoController.obtenerProductoByDetalleCarritoIdAndProductoId);


app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocs));


mongoose.connect(process.env.MONGO_URI)
  .then(() => {
    console.log('Conectado a MongoDB');
  })
  .catch(err => {
    console.error('Error al conectarse a MongoDB:', err.message);
  });

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
