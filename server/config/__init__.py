from datetime import timedelta
import os


class Config(object):
    SERVICE_NAME = '15th AppJam'

    PORT = 80
    DOMAIN = None

    SECRET_KEY = os.getenv('SECRET_KEY', 'ld02ifr9rj92ndi3n2vj9eo20')

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)
    JWT_HEADER_TYPE = 'JWT'

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_router': '/docs/',
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + 'API',
            'version': '1.0',
            'description': ''
        },

        'host': '{}:{}'.format(DOMAIN, PORT) if DOMAIN else None,
        'basePath': '/'
    }
