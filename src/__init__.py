import os
from flask import Flask
from config import Config
from src.endpoints import status, root

# Application Factory Function
def create_server(config_class=Config):
    app = Flask(__name__)

    # Configure the Flask application via CONFIGURATION_SETUP env
    config_type = os.getenv('CONFIGURATION_SETUP', default='config.DevelopmentConfig')
    app.config.from_object(config_type)

    # Add the status path
    @app.route("/", methods=['GET'])
    def root_endpoint():
        return root.end_point_root()

    # Add the status path
    @app.route("/status", methods=['GET'])
    def status_endpoint():
        return status.end_point_live()

    return app
