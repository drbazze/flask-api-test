import os

# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# TODO: The values should come from .env
# Default config class
class Config(object):
    """Default class config"""
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
# Testing config
class TestingConfig(Config):
    """Testing class config"""
    TESTING = True
# Development config
class DevelopmentConfig(Config):
    """Development class config"""
    DEBUG = True
# Production config
class ProductionConfig(Config):
    """Production class config"""
    FLASK_ENV = "production"
