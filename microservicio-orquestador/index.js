const express = require('express');
const axios = require('axios');
const { swaggerUi, swaggerDocs } = require('./swagger');  // Asegúrate de que la ruta a swagger.js sea correcta
const cors = require('cors'); 

const app = express();
const PORT = 4000;
app.use(cors());

app.use(express.json());

// Ruta para Swagger UI
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocs));

// Endpoints de la API
/**
 * @swagger
 * /:
 *   get:
 *     summary: Bienvenida a la API
 *     responses:
 *       200:
 *         description: Bienvenido a mi API
 */
app.get('/', (req, res) => {
  res.json({ message: 'Bienvenido a mi API' });
});

/**
 * @swagger
 * /api/orquestador/categorias:
 *   post:
 *     summary: Crear una nueva categoría
 *     tags: [Categorías]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               adminId:
 *                 type: integer
 *                 description: ID del administrador
 *               nombre:
 *                 type: string
 *                 description: Nombre de la categoría
 *               descripcion:
 *                 type: string
 *                 description: Descripción de la categoría
 *           example:  
 *             adminId: 1
 *             nombre: "Categoría de Prueba"
 *             descripcion: "Descripción de la categoría de prueba."
 *     responses:
 *       200:
 *         description: Categoría creada exitosamente
 *       404:
 *         description: Administrador no encontrado
 *       500:
 *         description: Error interno del servidor
 */
app.post('/api/orquestador/categorias', async (req, res) => {
  const { adminId, nombre, descripcion } = req.body;
  
  try {
    const adminResponse = await axios.get(`http://flask-backend:5000/admin/${adminId}`);
    
    if (adminResponse.status === 200) {
      const categoriaResponse = await axios.post('http://spring-backend:8081/api/categoria/postear', {
        nombre,
        descripcion
      });
      
      res.status(categoriaResponse.status).json({
        message: 'Categoría creada exitosamente',
        data: categoriaResponse.data
      });
    } else {
      res.status(404).json({ message: 'Administrador no encontrado' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Error interno del servidor', error: error.message });
  }
});

/**
 * @swagger
 * /api/orquestador/producto:
 *   post:
 *     summary: Crear un nuevo producto
 *     tags: [Productos]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               adminId:
 *                 type: integer
 *                 description: ID del administrador
 *               nombre:
 *                 type: string
 *                 description: Nombre del producto
 *               descripcion:
 *                 type: string
 *                 description: Descripción del producto
 *               precio:
 *                 type: number
 *                 format: float
 *                 description: Precio del producto
 *               stock:
 *                 type: integer
 *                 description: Cantidad en stock del producto
 *               categoriaId:
 *                 type: integer
 *                 description: ID de la categoría a la que pertenece el producto
 *           example:
 *             adminId: 1
 *             nombre: "Producto de Ejemplo"
 *             descripcion: "Descripción del producto de ejemplo."
 *             precio: 29.99
 *             stock: 100
 *             categoriaId: 2
 *     responses:
 *       200:
 *         description: Producto creado exitosamente
 *       404:
 *         description: Administrador no encontrado
 *       500:
 *         description: Error interno del servidor
 */
app.post('/api/orquestador/producto', async (req, res) => {
  const { adminId, nombre, descripcion, precio, stock, categoriaId } = req.body;
  
  try {
    const adminResponse = await axios.get(`http://flask-backend:5000/admin/${adminId}`);
    
    if (adminResponse.status === 200) {
      const productoResponse = await axios.post('http://spring-backend:8081/api/producto/postear', {
        nombre,
        descripcion,
        precio,
        stock,
        categoriaId
      });
      
      res.status(productoResponse.status).json({
        message: 'Producto creado exitosamente',
        data: productoResponse.data
      });
    } else {
      res.status(404).json({ message: 'Administrador no encontrado' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Error interno del servidor', error: error.message });
  }
});

/**
 * @swagger
 * /api/orquestador/categoria/eliminar:
 *   delete:
 *     summary: Eliminar una categoría
 *     tags: [Categorías]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               adminId:
 *                 type: integer
 *                 description: ID del administrador
 *               categoriaId:
 *                 type: integer
 *                 description: ID de la categoría a eliminar
 *           example:
 *             adminId: 1
 *             categoriaId: 3
 *     responses:
 *       200:
 *         description: Categoría eliminada correctamente
 *       404:
 *         description: Administrador no encontrado
 *       500:
 *         description: Error interno del servidor
 */
app.delete('/api/orquestador/categoria/eliminar', async (req, res) => {
  const { adminId, categoriaId } = req.body;
  
  try {
    const adminResponse = await axios.get(`http://flask-backend:5000/admin/${adminId}`);
    
    if (adminResponse.status === 200) {
      const categoriaResponse = await axios.delete(`http://spring-backend:8081/api/categoria/${categoriaId}`);
      
      res.status(categoriaResponse.status).json({
        message: 'Categoría eliminada correctamente',
        data: categoriaResponse.data
      });
    } else {
      res.status(404).json({ message: 'Administrador no encontrado' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Error interno del servidor', error: error.message });
  }
});

/**
 * @swagger
 * /api/orquestador/producto/eliminar:
 *   delete:
 *     summary: Eliminar un producto
 *     tags: [Productos]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               adminId:
 *                 type: integer
 *                 description: ID del administrador
 *               productoId:
 *                 type: integer
 *                 description: ID del producto a eliminar
 *           example:
 *             adminId: 1
 *             productoId: 42
 *     responses:
 *       200:
 *         description: Producto eliminado correctamente
 *       404:
 *         description: Administrador no encontrado
 *       500:
 *         description: Error interno del servidor
 */
app.delete('/api/orquestador/producto/eliminar', async (req, res) => {
  const { adminId, productoId } = req.body;
  
  try {
    const adminResponse = await axios.get(`http://flask-backend:5000/admin/${adminId}`);
    
    if (adminResponse.status === 200) {
      const productoResponse = await axios.delete(`http://spring-backend:8081/api/producto/${productoId}`);
      
      res.status(productoResponse.status).json({
        message: 'Producto eliminado correctamente',
        data: productoResponse.data
      });
    } else {
      res.status(404).json({ message: 'Administrador no encontrado' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Error interno del servidor', error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Orquestador de microservicios escuchando en el puerto ${PORT}. Documentación disponible en http://localhost:${PORT}/api-docs`);
});
