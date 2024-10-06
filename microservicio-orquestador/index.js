const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 4000; 

app.use(express.json());

app.post('/api/orquestador/categorias', async (req, res) => {
    const { adminId, nombre, descripcion } = req.body;

    console.log(`Recibiendo solicitud para adminId: ${adminId}, nombre: ${nombre}, descripcion: ${descripcion}`);

    try {
        const adminResponse = await axios.get(`http://localhost:5000/admin/${adminId}`);
        console.log(`Respuesta del servicio de administrador:`, adminResponse.data);
        
        if (adminResponse.status === 200) {
            const adminData = adminResponse.data;
            console.log(`Administrador encontrado: ${adminData.nombre}`);

            const categoriaResponse = await axios.post('http://localhost:8081/api/categoria/postear', {
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

app.post('/api/orquestador/producto', async)


app.listen(PORT, () => {
    console.log(`Orquestador de microservicios escuchando en el puerto ${PORT}`);
});
