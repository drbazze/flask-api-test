import os

# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Default config class
class Config(object):
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
# Testing config
class TestingConfig(Config):
    TESTING = True
# Development config
class DevelopmentConfig(Config):
    DEBUG = True
# Production config
class ProductionConfig(Config):
    FLASK_ENV = "production"
