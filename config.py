import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maxa:maxa12345@localhost/myblog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    

class ProdConfig(Config):
    pass

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maxa:maxa12345@localhost/myblog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}