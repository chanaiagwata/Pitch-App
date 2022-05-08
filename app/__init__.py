from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    
    #creating configurations
    app.config.from_object(config_options[config_name])
    
    #Initialize extensions
    bootstrap.init_app(app)
    
    
    #views and forms go here
    
    
    return app