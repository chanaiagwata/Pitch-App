from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy




bootstrap = Bootstrap()
db = SQLAlchemy()

# Initializing application
def create_app(config_name):
    app = Flask(__name__)
    
    #creating configurations
    app.config.from_object(config_options[config_name])
    
    #Initialize extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    
    #register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    return app