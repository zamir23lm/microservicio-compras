const mongoose = require('mongoose');

const CarritoSchema = new mongoose.Schema({
    _id: { type: mongoose.Schema.Types.ObjectId, auto: true },
    usuario_id: { type: String, required: true },
    carritoDetalle_id: { type: mongoose.Schema.Types.ObjectId, ref: 'DetalleCarrito', required: false },
    estado : { type: String, required: true, default: 'pendiente' },
    fecha: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Carrito', CarritoSchema);