const DetalleCarritoService = require('../domain/services/DetalleCarritoService');
const mongoose = require('mongoose');

class DetalleCarritoController {
    
    /**
     * @swagger
     * /api/detalleCarrito/postear:
     *   post:
     *     summary: Crear un nuevo detalle del carrito
     *     tags: [DetalleCarrito]
     *     requestBody:
     *       required: true
     *       content:
     *         application/json:
     *           schema:
     *             type: object
     *             properties:
     *               productos:
     *                 type: array
     *                 items:
     *                   type: object
     *                   properties:
     *                     producto_id:
     *                       type: number
     *                     cantidad:
     *                       type: number
     *                     precioUnitario:
     *                       type: number
     *             example:
     *               productos: [{ producto_id: 101, cantidad: 2, precioUnitario: 50.00 }]
     *     responses:
     *       201:
     *         description: Detalle del carrito creado exitosamente
     *       400:
     *         description: Error en la solicitud
     */
    async crearDetalleCarrito(req, res) {
        try {
            const detalleCarrito = await DetalleCarritoService.crearDetalleCarrito(req.body);
            res.status(201).json(detalleCarrito);
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }

    /**
     * @swagger
     * /api/detalleCarrito/agregarProducto/{id}:
     *   put:
     *     summary: Agregar un producto al detalle del carrito
     *     tags: [DetalleCarrito]
     *     parameters:
     *       - name: id
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del detalle del carrito
     *     requestBody:
     *       required: true
     *       content:
     *         application/json:
     *           schema:
     *             type: object
     *             properties:
     *               producto_id:
     *                 type: number
     *               cantidad:
     *                 type: number
     *               precioUnitario:
     *                 type: number
     *             example:
     *               producto_id: 103
     *               cantidad: 3
     *               precioUnitario: 10.00
     *     responses:
     *       200:
     *         description: Producto agregado exitosamente
     *       400:
     *         description: Error al agregar producto
     */
    async agregarProducto(req, res) {
        try {
            const { id } = req.params;
            const producto = req.body;
            const detalleCarrito = await DetalleCarritoService.agregarProducto(id, producto);
            res.status(200).json(detalleCarrito);
        } catch (err) {
            res.status(400).json({ message: err.message });
        }
    }

    /**
     * @swagger
     * /api/detalleCarrito/all:
     *   get:
     *     summary: Obtener todos los detalles del carrito
     *     tags: [DetalleCarrito]
     *     responses:
     *       200:
     *         description: Lista de todos los detalles del carrito
     *       400:
     *         description: Error al obtener los detalles del carrito
     */
    async obtenerTodosLosDetallesCarrito(req, res) {
        try {
            const detallesCarrito = await DetalleCarritoService.obtenerTodosLosDetallesCarrito();
            res.status(200).json(detallesCarrito);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }

    /**
     * @swagger
     * /api/detalleCarrito/{id}:
     *   get:
     *     summary: Obtener detalle del carrito por ID
     *     tags: [DetalleCarrito]
     *     parameters:
     *       - name: id
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del detalle del carrito
     *     responses:
     *       200:
     *         description: Detalle del carrito obtenido exitosamente
     *       400:
     *         description: Error al obtener el detalle del carrito
     */
    async obtenerDetalleCarritoPorId(req, res) {
        try {
            const { id } = req.params;
            const detalleCarrito = await DetalleCarritoService.obtenerDetalleCarritoPorId(id);
            res.status(200).json(detalleCarrito);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }

    /**
     * @swagger
     * /api/detalleCarrito/{id}/{productoid}:
     *   delete:
     *     summary: Eliminar un producto del detalle del carrito
     *     tags: [DetalleCarrito]
     *     parameters:
     *       - name: id
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del detalle del carrito
     *       - name: productoid
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del producto
     *     responses:
     *       200:
     *         description: Producto eliminado exitosamente
     *       400:
     *         description: Error al eliminar el producto
     */
    async eliminarProducto(req, res) {
        try {
            const { id } = req.params;
            const { productoid } = req.params;
            const detalleCarrito = await DetalleCarritoService.eliminarProducto(id, productoid);
            res.status(200).json(detalleCarrito);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }

    /**
     * @swagger
     * /api/detalleCarrito/{id}:
     *   delete:
     *     summary: Eliminar un detalle del carrito
     *     tags: [DetalleCarrito]
     *     parameters:
     *       - name: id
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del detalle del carrito
     *     responses:
     *       204:
     *         description: Detalle del carrito eliminado exitosamente
     *       400:
     *         description: Error al eliminar el detalle del carrito
     */
    async eliminarDetalleCarrito(req, res) {
        try {
            const { id } = req.params;
            await DetalleCarritoService.eliminarDetalleCarrito(id);
            res.status(204).end();
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }

    /**
     * @swagger
     * /api/detalleCarrito/{id}/{productoid}:
     *   put:
     *     summary: Editar la cantidad de un producto en el detalle del carrito
     *     tags: [DetalleCarrito]
     *     parameters:
     *       - name: id
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del detalle del carrito
     *       - name: productoid
     *         in: path
     *         required: true
     *         schema:
     *           type: string
     *         description: ID del producto
     *     requestBody:
     *       required: true
     *       content:
     *         application/json:
     *           schema:
     *             type: object
     *             properties:
     *               cantidad:
     *                 type: number
     *             example:
     *               cantidad: 5
     *     responses:
     *       200:
     *         description: Cantidad editada exitosamente
     *       400:
     *         description: Error al editar la cantidad
     */
    async editarCantidadProducto(req, res) {
        try {
            const { id } = req.params;
            const { productoid } = req.params;
            const { cantidad } = req.body;
            const detalleCarrito = await DetalleCarritoService.editarCantidadProducto(id, productoid, cantidad);
            res.status(200).json(detalleCarrito);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }
    /**
 * @swagger
 * /api/detalleCarrito/{id}/{productoid}:
 *   get:
 *     summary: Obtener un producto específico por el ID del detalle del carrito y el ID del producto
 *     tags: [DetalleCarrito]
 *     parameters:
 *       - name: id
 *         in: path
 *         required: true
 *         schema:
 *           type: string
 *         description: ID del detalle del carrito
 *       - name: productoid
 *         in: path
 *         required: true
 *         schema:
 *           type: string
 *         description: ID del producto en el detalle del carrito
 *     responses:
 *       200:
 *         description: Producto obtenido exitosamente
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 producto_id:
 *                   type: number
 *                 cantidad:
 *                   type: number
 *                 precioUnitario:
 *                   type: number
 *               example:
 *                 producto_id: 103
 *                 cantidad: 3
 *                 precioUnitario: 10.00
 *       400:
 *         description: Error al obtener el producto del detalle del carrito
 */
    async obtenerProductoByDetalleCarritoIdAndProductoId(req, res) {
        try {
            const { id } = req.params;
            const { productoid } = req.params;
            const detalleCarrito = await DetalleCarritoService.obtenerProductoByDetalleCarritoIdAndProductoId(id, productoid);
            res.status(200).json(detalleCarrito);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }

}

module.exports = new DetalleCarritoController();
