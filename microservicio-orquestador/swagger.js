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
    apis: ['app.js', 'routes/*.js'], // Incluye todos los archivos de rutas aquí
  };
  