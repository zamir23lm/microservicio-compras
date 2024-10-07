require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();

const corsOptions = {
  origin: "*",
  methods: "GET,POST,PUT,DELETE",
};
app.use(cors(corsOptions));


app.use(express.json());

const CarritoController = require('./src/carrito/controllers/CarritoController');
const DetalleCarritoController = require('./src/detalleCarrito/controllers/DetalleCarritoController');
const { swaggerUi, swaggerDocs } = require('./swagger');

// Rutas de prueba
app.get('/', (req, res) => {
  res.json({ message: 'Bienvenido a mi API' });
});
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);  // Log de método y URL de la solicitud
  next();
});

app.post('/api/carrito/postear', (req, res) => {
  console.log('Solicitud recibida en /api/carrito/postear:', req.body);  // Log del cuerpo de la solicitud
  res.json({ message: 'Carrito creado exitosamente' });
});


// Rutas de carrito
app.post('/api/carrito/postear', CarritoController.createCarrito);
app.get('/api/carrito/all', CarritoController.obtenerTodosLosCarritos);
app.get('/api/carrito/:id', CarritoController.obtenerCarritoPorId);
app.get('/api/carrito/usuario/:usuarioId', CarritoController.obtenerCarritosPorUsuario);
app.put('/api/carrito/pagado/:id', CarritoController.modificarCarritoPagado);
app.delete('/api/carrito/:id', CarritoController.eliminarCarrito);
app.put('/api/carrito/detalles/:id', CarritoController.editarDetalleCarrito);

// Rutas de detalle carrito
app.post('/api/detalleCarrito/postear', DetalleCarritoController.crearDetalleCarrito);
app.put('/api/detalleCarrito/agregarProducto/:id', DetalleCarritoController.agregarProducto);
app.get('/api/detalleCarrito/all', DetalleCarritoController.obtenerTodosLosDetallesCarrito);
app.get('/api/detalleCarrito/:id', DetalleCarritoController.obtenerDetalleCarritoPorId);
app.delete('/api/detalleCarrito/:id', DetalleCarritoController.eliminarDetalleCarrito);
app.delete('/api/detalleCarrito/:id/:productoid', DetalleCarritoController.eliminarProducto);
app.put('/api/detalleCarrito/:id/:productoid', DetalleCarritoController.editarCantidadProducto);
app.get('/api/detalleCarrito/:id/:productoid', DetalleCarritoController.obtenerProductoByDetalleCarritoIdAndProductoId);

// Swagger documentation
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocs));

// Conexión a MongoDB
mongoose.connect('mongodb://98.83.127.213:27017/compras')
  .then(() => {
    console.log('Conectado a MongoDB');
  })
  .catch(err => {
    console.error('Error al conectarse a MongoDB:', err.message);
  });

// Iniciar servidor
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
