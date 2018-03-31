from config import Config


class DevConfig(Config):
    HOST = 'localhost'

    if Config.DOMAIN is None:
        Config.SWAGGER['host'] = '{}:{}'.format(HOST, Config.PORT)

    DEBUG = True

    MONGODB_SETTINGS = {
        'host': HOST,
        'port': 27017,
        'db': Config.SERVICE_NAME
    }
