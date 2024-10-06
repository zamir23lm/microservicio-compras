# Configuración de Swagger
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Administradores",
        "description": "Documentación de la API para gestionar administradores.",
        "version": "1.0.0",
        "contact": {
            "name": "Soporte",
            "url": "http://tu-app-soporte.com"
        }
    },
    "basePath": "/",
    "schemes": ["http"],
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'swagger',  # Cambiado de 'swagger.json' a 'swagger'
            "route": '/swagger.json',  # Esta ruta se mantiene igual
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

swaggerui_blueprint = get_swaggerui_blueprint(
    swagger_config['specs_route'],  # Ruta base
    swagger_config['specs'][0]['route'],  # Ruta al JSON
    config={'app_name': swagger_template['info']['title']}  # Nombre de la aplicación
)

app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_config['static_url_path'])
