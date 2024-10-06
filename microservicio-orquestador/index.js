const express = require('express');
const axios = require('axios');
const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const app = express();
const PORT = 4000;

app.use(express.json());

const swaggerOptions = {
  swaggerDefinition: {
    info: {
      title: 'API de Orquestador de Microservicios',
      version: '1.0.0',
      description: 'Documentación de los servicios del Orquestador de Microservicios',
      contact: {
        name: 'Soporte',
        url: 'http://tu-app-soporte.com',
      },
    },
    servers: [
      {
        url: `http://localhost:${PORT}`,
        description: 'Servidor local',
      },
    ],
  },
  apis: ['index.js'], 
};

const swaggerDocs = swaggerJsdoc(swaggerOptions);
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
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               adminId:
 *                 type: integer
 *               nombre:
 *                 type: string
 *               descripcion:
 *                 type: string
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

    console.log(`Recibiendo solicitud para adminId: ${adminId}, nombre: ${nombre}, descripcion: ${descripcion}`);
    try {
        const adminResponse = await axios.get(`http://flask-backend:5000/admin/${adminId}`);
        console.log(`Respuesta del servicio de administrador:`, adminResponse.data);
        
        if (adminResponse.status === 200) {
            const adminData = adminResponse.data;
            console.log(`Administrador encontrado: ${adminData.nombre}`);

            const categoriaResponse = await axios.post('http://spring-backend:8081/api/categoria/postear', {
                nombre: nombre,
                descripcion: descripcion
            });

            res.status(categoriaResponse.status).json({
                message: 'Categoría creada exitosamente',
                data: categoriaResponse.data
            });
        } else {
            res.status(404).json({ message: 'Administrador no encontrado' });
        }
    } catch (error) {
        console.error(`Error al buscar administrador o crear categoría:`, error);

        if (error.response && error.response.status === 404) {
            res.status(404).json({ message: 'Administrador no encontrado' });
        } else {
            res.status(500).json({ message: 'Error interno del servidor' });
        }
    }
});

/**
 * @swagger
 * /api/orquestador/producto:
 *   post:
 *     summary: Crear un nuevo producto
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               adminId:
 *                 type: integer
 *               nombre:
 *                 type: string
 *               descripcion:
 *                 type: string
 *               precio:
 *                 type: number
 *               stock:
 *                 type: integer
 *               categoriaId:
 *                 type: integer
 *     responses:
 *       200:
 *         description: Producto creado exitosamente
 *       404:
 *         description: Administrador no encontrado
 *       500:
 *         description: Error interno del servidor
 */
app.post('/api/orquestador/producto', async(req, res) => {
    const {adminId, nombre, descripcion, precio, stock, categoriaId} = req.body;
    console.log("Recibiendo informacion");
    try{
        const adminResponse = await axios.get(`http://flask-backend:5000/admin/${adminId}`)
        console.log("Respuesta del microservicio administrador", adminResponse.data);
        if(adminResponse.status ===200){
            const adminData = adminResponse.data;
            const productoResponse = await axios.post('http://spring-backend:8081/api/producto/postear', {
                nombre:nombre,
                descripcion:descripcion,
                precio:precio,
                stock:stock,
                categoriaId:categoriaId
                
            });
            res.status(productoResponse.status).json({
                message:'Producto creado exitosamente',
                data:productoResponse.data
            });
        }else{
            res.status(404).json({message:'Administrador no encontrado'});
        }
    }catch(error){
        console.error('Error al buscar al administrador o al momento de crear el producto', error);
        if (error.response) {
            if (error.response.status === 404) {
                res.status(404).json({ message: 'Administrador no encontrado' });
            } else {
                res.status(error.response.status).json({ message: 'Error en la creación del producto', error: error.message });
            }
        } else {
            res.status(500).json({ message: 'Error interno en el servidor' });
        }
    }

});

/**
 * @swagger
 * /api/orquestador/categoria/eliminar:
 *   delete:
 *     summary: Eliminar una categoría
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               adminId:
 *                 type: integer
 *               categoriaId:
 *                 type: integer
 *     responses:
 *       200:
 *         description: Categoría eliminada correctamente
 *       404:
 *         description: Administrador no encontrado
 *       500:
 *         description: Error interno del servidor
 */
app.delete('/api/orquestador/categoria/eliminar/', async(req, res)=>{
    const{adminId, categoriaId} = req.body;
    try{
        const adminResponse = await axios.get(`http://flask-backend:5000/admin/${adminId}`);
        if(adminResponse.status === 200){
            const categoriaResponse = await axios.delete(`http://spring-backend:8081/api/categoria/${categoriaId}`)
            res.status(categoriaResponse.status).json({
                message:"Categoria eliminada correctamente",
                data:categoriaResponse.data
            });
        }else{
            res.status(404).json({message:'Administrador no encontrado'});
        }
    }
    catch(error){
        if(error.response){
            if(error.response.status ===404){
                res.status(404).json({message:'Administrador no encontrado'});
            }else{
                res.status(error.response.status).json({message:'Error al eliminar la categoría', error: error.message});
            }
        }else{
            res.status(500).json({message:'Error interno del microservicio orquestador'});
        }
    }
});

/**
 * @swagger
 * /api/orquestador/producto/eliminar:
 *   delete:
 *     summary: Eliminar un producto
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               adminId:
 *                 type: integer
 *               productoId:
 *                 type: integer
 *     responses:
 *       200:
 *         description: Producto eliminado correctamente
 *       404:
 *         description: Administrador no encontrado
 *       500:
 *         description: Error interno del servidor
 */
app.delete('/api/orquestador/producto/eliminar/', async(req, res)=>{
    const{adminId, productoId} = req.body;
    try{
        const adminResponse = await axios.get(`http://flask-backend:5000/admin/${adminId}`);
        if(adminResponse.status === 200){
            const productoResponse = await axios.delete(`http://spring-backend:8081/api/producto/${productoId}`)
            res.status(productoResponse.status).json({
                message:"Producto eliminado correctamente",
                data:productoResponse.data
            });
        }else{
            res.status(404).json({message:'Administrador no encontrado'});
        }
    }
    catch(error){
        if(error.response){
            if(error.response.status ===404){
                res.status(404).json({message:'Administrador no encontrado'});
            }else{
                res.status(error.response.status).json({message:'Error al eliminar el producto', error: error.message});
            }
        }else{
            res.status(500).json({message:'Error interno del microservicio orquestador'});
        }
    }
});

app.listen(PORT, () => {
    console.log(`Orquestador de microservicios escuchando en el puerto ${PORT}`);
});
