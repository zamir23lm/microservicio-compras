const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 4000; 

app.use(express.json());

app.get('/', (req, res) => {
    res.json({ message: 'Bienvenido a mi API' });
});

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

app.post('/api/orquestador/producto', async(req, res) => {
    const {adminId, nombre, descripcion, precio, stock, categoriaId} = req.body;
    console.log("Recibiendo informacion");
    try{
        const adminResponse = await axios.get(`http://localhost:5000/admin/${adminId}`)
        console.log("Respuesta del microservicio administrador", adminResponse.data);
        if(adminResponse.status ===200){
            const adminData = adminResponse.body;
            const productoResponse = await axios.post('http://localhost:8081/api/producto/postear', {
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
            res.status(404).json({message:'Administrador no encontradoo'});
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

app.delete('/api/orquestador/categoria/eliminar/', async(req, res)=>{
    const{adminId, categoriaId} = req.body;
    try{
        const adminResponse = await axios.get(`http://localhost:5000/admin/${adminId}`);
        if(adminResponse.status === 200){
            const categoriaResponse = await axios.delete(`http://localhost:8081/api/categoria/${categoriaId}`)
            res.status(categoriaResponse.status).json({
                message:"Categoria elimianda correctamente",
                data:categoriaResponse.data
            });
        }else{
            res.status(404).json({message:'Adminitrador no encontrado'});
        }
    }
    catch(error){
        if(error.response){
            if(error.response.status ===404){
                res.status(404).json({message:'Administrador no encontrado'});
            }else{
                res.status(error.response.status).json({message:'Error aleliminar la categoria', error: error.message});
            }
        }else{
            res.status(500).json({message:'Error interno del del microservicio orquestador'});
        }
    }
});

app.delete('/api/orquestador/producto/eliminar/', async(req, res)=>{
    const{adminId, productoId} = req.body;
    try{
        const adminResponse = await axios.get(`http://localhost:5000/admin/${adminId}`);
        if(adminResponse.status === 200){
            const productoResponse = await axios.delete(`http://localhost:8081/api/producto/${productoId}`)
            res.status(productoResponse.status).json({
                message:"Producto elimiando correctamente",
                data:productoResponse.data
            });
        }else{
            res.status(404).json({message:'Adminitrador no encontrado'});
        }
    }
    catch(error){
        if(error.response){
            if(error.response.status ===404){
                res.status(404).json({message:'Administrador no encontrado'});
            }else{
                res.status(error.response.status).json({message:'Error aleliminar el producto', error: error.message});
            }
        }else{
            res.status(500).json({message:'Error interno del del microservicio orquestador'});
        }
    }
});


app.listen(PORT, () => {
    console.log(`Orquestador de microservicios escuchando en el puerto ${PORT}`);
});
