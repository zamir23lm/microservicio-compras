require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');  // Importa el middleware CORS
const app = express();

// Configuración de CORS
app.use(cors({
  origin: '*',  // Permite cualquier origen
  methods: ['GET', 'POST', 'PUT', 'DELETE'],  // Métodos permitidos
  allowedHeaders: ['Content-Type', 'Authorization'],  // Cabeceras permitidas
  credentials: true  // Permitir uso de credenciales si es necesario
}));

// Manejar solicitudes preflight (OPTIONS)
app.options('*', cors());  // Permitir solicitudes preflight de todos los orígenes

// Asegurar que las cabeceras CORS están presentes en todas las respuestas
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');  // Permitir cualquier origen
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

// Middleware para manejar JSON en las solicitudes
app.use(express.json()); 

// Importación de controladores
const CarritoController = require('./src/carrito/controllers/CarritoController');
const DetalleCarritoController = require('./src/detalleCarrito/controllers/DetalleCarritoController');
const { swaggerUi, swaggerDocs } = require('./swagger');

// Rutas de prueba
app.get('/', (req, res) => {
  res.json({ message: 'Bienvenido a mi API' });
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
