from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

# Initializing application
def create_app(config_name):
    app = Flask(__name__)
    
    #creating configurations
    app.config.from_object(config_options[config_name])
    
    #Initialize extensions
    bootstrap.init_app(app)
    
    
    #views and forms go here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app