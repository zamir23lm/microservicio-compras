const CarritoService = require('../domain/services/CarritoService');
const mongoose = require('mongoose');

class CarritoController {

    /**
     * @swagger
     * /api/carrito/postear:
     *   post:
     *     summary: Crear un nuevo carrito
     *     tags: [Carrito]
     *     requestBody:
     *       required: true
     *       content:
     *         application/json:
     *           schema:
     *             type: object
     *             properties:
     *               usuario_id:
     *                 type: string
     *                 description: ID del usuario
     *               estado:
     *                 type: string
     *                 description: Estado del carrito
     *             example:
     *               usuario_id: "user123"
     *               estado: "pendiente"
     *     responses:
     *       201:
     *         description: Carrito creado exitosamente
     *       400:
     *         description: Error de validación
     */
    async createCarrito(req, res) {
        try {
            const carrito = CarritoService.createCarrito(req.body);
            res.status(201).json(carrito);
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }

    /**
     * @swagger
     * /api/carrito/all:
     *   get:
     *     summary: Obtener todos los carritos
     *     tags: [Carrito]
     *     responses:
     *       200:
     *         description: Lista de todos los carritos
     *         content:
     *           application/json:
     *             schema:
     *               type: array
     *               items:
     *                 type: object
     *       400:
     *         description: Error al obtener los carritos
     */
    async obtenerTodosLosCarritos(req, res) {
        try {
            const carritos = await CarritoService.obtenerTodosLosCarritos();
            res.status(200).json(carritos);
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }

    /**
     * @swagger
     * /api/carrito/{id}:
     *   get:
     *     summary: Obtener carrito por ID
     *     tags: [Carrito]
     *     parameters:
     *       - name: id
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del carrito
     *     responses:
     *       200:
     *         description: Carrito obtenido exitosamente
     *       400:
     *         description: Error al obtener el carrito
     */
    async obtenerCarritoPorId(req, res) {
        try {
            const { id } = req.params;
            const carrito = await CarritoService.obtenerCarritoPorId(id);
            res.status(200).json(carrito);
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }

    /**
     * @swagger
     * /api/carrito/usuario/{usuarioId}:
     *   get:
     *     summary: Obtener carritos por usuario
     *     tags: [Carrito]
     *     parameters:
     *       - name: usuarioId
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del usuario
     *     responses:
     *       200:
     *         description: Carritos obtenidos exitosamente
     *       400:
     *         description: Error al obtener los carritos
     */
    async obtenerCarritosPorUsuario(req, res) {
        try {
            const { usuarioId } = req.params;
            const carritos = await CarritoService.obtenerCarritosPorUsuario(usuarioId);
            res.status(200).json(carritos);
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }

    /**
     * @swagger
     * /api/carrito/pagado/{id}:
     *   put:
     *     summary: Modificar carrito a pagado
     *     tags: [Carrito]
     *     parameters:
     *       - name: id
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del carrito
     *     responses:
     *       200:
     *         description: Carrito modificado exitosamente
     *       400:
     *         description: Error al modificar el carrito
     */
    async modificarCarritoPagado(req, res) {
        try {
            const { id } = req.params;
            const carrito = await CarritoService.modificarCarritoPagado(id);
            res.status(200).json(carrito);
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }

    /**
     * @swagger
     * /api/carrito/{id}:
     *   delete:
     *     summary: Eliminar carrito
     *     tags: [Carrito]
     *     parameters:
     *       - name: id
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del carrito
     *     responses:
     *       204:
     *         description: Carrito eliminado exitosamente
     *       400:
     *         description: Error al eliminar el carrito
     */
    async eliminarCarrito(req, res) {
        try {
            const { id } = req.params;
            await CarritoService.eliminarCarrito(id);
            res.status(204).end();
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }

    /**
     * @swagger
     * /api/carrito/detalles/{id}:
     *   put:
     *     summary: Editar el ID del detalle del carrito
     *     tags: [Carrito]
     *     parameters:
     *       - name: id
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del carrito
     *       - name: detallesCarritoId
     *         in: query
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del detalle del carrito
     *     responses:
     *       200:
     *         description: Carrito modificado exitosamente
     *       400:
     *         description: Error al modificar el carrito
     */
    async editarDetalleCarrito(req, res) {
        try {
            const { detallesCarritoId } = req.query;
            const { id } = req.params;

            // Verifica si el detallesCarritoId es un ObjectId válido
            if (!mongoose.Types.ObjectId.isValid(detallesCarritoId)) {
                return res.status(400).json({ message: "El detallesCarritoId no es un ObjectId válido" });
            }

            const carrito = await CarritoService.editarDetalleCarrito(id, detallesCarritoId);
            res.status(200).json(carrito);
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }

}

module.exports = new CarritoController();
