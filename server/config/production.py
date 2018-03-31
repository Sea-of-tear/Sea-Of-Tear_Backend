import socket

from config import Config


class ProductionConfig(Config):
    HOST = socket.gethostbyname(socket.gethostname())

    if Config.DOMAIN is not None:
        Config.SWAGGER['host'] = '{}:{}'.format(HOST, Config.PORT)

    MONGODB_SETTINGS = {
        'HOST': HOST,
        'PORT': 27017,
        'db': Config.SERVICE_NAME
    }
