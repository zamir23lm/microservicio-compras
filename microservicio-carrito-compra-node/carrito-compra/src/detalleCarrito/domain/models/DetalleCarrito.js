const mongoose = require('mongoose');

const ProductoSchema = new mongoose.Schema({
    producto_id: { type: Number, required: true },
    cantidad: { type: Number, required: true, min: 1 },
    precioUnitario: { type: Number, required: true }
});

const DetalleCarritoSchema = new mongoose.Schema({
    _id: { type: mongoose.Schema.Types.ObjectId, auto: true },
    productos: [ProductoSchema],
    total: { type: Number, default: 0 }
});

DetalleCarritoSchema.methods.calcularTotal = function () {
    this.total = this.productos.reduce((acc, prod) => {
        return acc + (prod.precioUnitario * prod.cantidad);
    }, 0);
};

module.exports = mongoose.model('DetalleCarrito', DetalleCarritoSchema);