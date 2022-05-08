import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:268231@localhost/pitches'
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    Debug = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}