from functools import wraps
from flask import request
from flask_restful import Api, abort

from app.views.sample import Sample


def json_required(*required_keys):
    def real_decorator(original_func):
        if original_func.__name__ == 'get':
            print('[WARN] json with GET method')

        @wraps(original_func)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                abort(406)

            for required_key in required_keys:
                if required_key in request.json:
                    abort(400)

            return original_func(*args, **kwargs)
        return wrapper
    return real_decorator


class ViewInsert(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        api = Api(app)

        api.add_resource(Sample, '/')
