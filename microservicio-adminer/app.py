from flask import Flask, request, jsonify
from models import db, Administrador
from config import Config
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger
from flask_cors import CORS  

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)  

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)
with app.app_context():
    db.create_all()

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

# Registro del blueprint de Swagger UI
swaggerui_blueprint = get_swaggerui_blueprint(
    swagger_config['specs_route'],  # Ruta base
    swagger_config['specs'][0]['route'],  # Ruta al JSON
    config={'app_name': swagger_template['info']['title']}  # Nombre de la aplicación
)

app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_config['static_url_path'])

# Inicialización de Swagger
swagger = Swagger(app, template=swagger_template, config=swagger_config)

@app.route('/')
def index():
    """
    Bienvenida al API de Administradores
    ---
    responses:
      200:
        description: Bienvenido al microservicio de Administrador
    """
    return jsonify({"message": "Bienvenido al microservicio de Administrador"}), 200

@app.route('/admin', methods=['POST'])
def create_admin():
    """
    Crear un nuevo administrador
    ---
    tags:
      - Administrador
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
            email:
              type: string
            password:
              type: string
    responses:
      201:
        description: Administrador creado exitosamente
      400:
        description: Error en la solicitud
    """
    data = request.get_json()
    nuevo_admin = Administrador(nombre=data['nombre'], email=data['email'], password=data['password'])
    db.session.add(nuevo_admin)
    db.session.commit()
    return jsonify({"message": "Administrador creado exitosamente"}), 201

@app.route('/admins', methods=['GET'])
def get_admins():
    """
    Obtener la lista de administradores
    ---
    tags:
      - Administrador
    responses:
      200:
        description: Lista de administradores
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              nombre:
                type: string
              email:
                type: string
    """
    administradores = Administrador.query.all()
    return jsonify([{"id": admin.id, "nombre": admin.nombre, "email": admin.email} for admin in administradores]), 200

@app.route('/admin/<int:id>', methods=['GET'])
def get_admin(id):
    """
    Obtener un administrador por ID
    ---
    tags:
      - Administrador
    parameters:
      - name: id
        in: path
        required: true
        type: integer
        description: ID del administrador
    responses:
      200:
        description: Administrador encontrado
        schema:
          properties:
            id:
              type: integer
            nombre:
              type: string
            email:
              type: string
      404:
        description: Administrador no encontrado
    """
    admin = Administrador.query.get_or_404(id)
    return jsonify({"id": admin.id, "nombre": admin.nombre, "email": admin.email}), 200

@app.route('/admin/<int:id>', methods=['PUT'])
def update_admin(id):
    """
    Actualizar un administrador
    ---
    tags:
      - Administrador
    parameters:
      - name: id
        in: path
        required: true
        type: integer
        description: ID del administrador
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
            email:
              type: string
            password:
              type: string
    responses:
      200:
        description: Administrador actualizado correctamente
      404:
        description: Administrador no encontrado
    """
    admin = Administrador.query.get_or_404(id)
    data = request.get_json()
    admin.nombre = data['nombre']
    admin.email = data['email']
    admin.password = data['password']
    db.session.commit()
    return jsonify({"message": "Administrador actualizado correctamente"}), 200

@app.route('/admin/<int:id>', methods=['DELETE'])
def delete_admin(id):
    """
    Eliminar un administrador
    ---
    tags:
      - Administrador
    parameters:
      - name: id
        in: path
        required: true
        type: integer
        description: ID del administrador
    responses:
      200:
        description: Administrador eliminado exitosamente
      404:
        description: Administrador no encontrado
    """
    admin = Administrador.query.get_or_404(id)
    db.session.delete(admin)
    db.session.commit()
    return jsonify({"message": "Administrador eliminado exitosamente"}), 200

@app.route('/admin/login', methods=['POST'])
def login():
    """
    Iniciar sesión como administrador
    ---
    tags:
      - Administrador
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
            password:
              type: string
    responses:
      200:
        description: Inicio de sesión exitoso
      401:
        description: Credenciales inválidas
    """
    data = request.get_json()
    admin = Administrador.query.filter_by(email=data['email']).first()
    if admin is None or admin.password != data['password']:
        return jsonify({"message": "Credenciales inválidas"}), 401
    return jsonify({"message": "Inicio de sesión exitoso"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
