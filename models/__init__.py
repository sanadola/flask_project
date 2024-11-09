from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from config import Config
from routes.user import api

db = SQLAlchemy()
jwt = JWTManager()
swagger = Swagger()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SWAGGER'] = {
        'title': 'Flask CRUD API',
        'uiversion': 3,
        'version': '1.0',
        'description': 'A simple Flask CRUD API with JWT authentication',
        'specs_route': '/docs/',
        'securityDefinitions': {
            'Bearer': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
                'description': 'JWT Authorization header using the Bearer scheme. Example: "Bearer {token}"'
            }
        },
        'security': [{'Bearer': []}]
    }

    db.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)
    app.register_blueprint(api)

    return app