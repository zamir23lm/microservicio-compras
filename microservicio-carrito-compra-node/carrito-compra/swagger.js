const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

// Definimos las opciones de configuración
const swaggerOptions = {
    swaggerDefinition: {
        openapi: '3.0.0',
        info: {
            title: 'Carrito de Compras API',
            version: '1.0.0',
            description: 'API para manejar el carrito de compras y sus detalles',
            contact: {
                name: 'Zamir',
                email: 'tuemail@example.com'
            }
        },
        servers: [
            {
                url: 'http://localhost:3000',
                description: 'Servidor de desarrollo'
            }
        ]
    },
    apis: ['./src/**/*.js'],  
};

const swaggerDocs = swaggerJsdoc(swaggerOptions);

module.exports = {
    swaggerUi,
    swaggerDocs
};
