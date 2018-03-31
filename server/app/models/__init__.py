from mongoengine import *


class ModelInsert(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        settings = app.config['MONGODB_SETTINGS']

        connect(settings['db'], settings['HOST'], settings['PORT'])
