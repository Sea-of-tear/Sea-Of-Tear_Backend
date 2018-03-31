from flask import Response
from flask_restful import Resource


class Sample(Resource):
    def get(self):
        return Response('success', 200)
