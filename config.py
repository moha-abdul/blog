import os

class Config:
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maxa:maxa12345@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_MAROON_URL")
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maxa:maxa12345@localhost/pitches'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}