# app configurations
import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY')

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

config_options = {
    "dev_config": DevConfig,
    "prod_config": ProdConfig
}