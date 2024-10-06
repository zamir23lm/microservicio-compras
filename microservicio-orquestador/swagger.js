const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const swaggerOptions = {
  swaggerDefinition: {
    openapi: '3.0.0',  
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
        url: `http://localhost:4000`,
        description: 'Servidor de desarrollo',
      },
    ],
  },
  apis: ['./index.js'],
};

const swaggerDocs = swaggerJsdoc(swaggerOptions);

module.exports = {
  swaggerUi,
  swaggerDocs
};
