from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


from app.models.user import UserModel
from app.views import json_required


class Signup(Resource):
    @json_required('id', 'pw', 'email', 'nickname')
    def post(self):
        id = request.form['id']
        pw = request.form['pw']
        email = request.form['email']
        nickname = request.json['nickname']

        if UserModel.objects(id=id):
            return Response('id duplicate', 204)

        UserModel(id=id, pw=pw, email=email, nickname=nickname).save()

        return Response('signup success', 201)


class Login(Resource):
    @json_required('id', 'pw')
    def post(self):
        id = request.form['id']
        pw = request.form['pw']

        if UserModel(id=id, pw=pw):
            return {
                'access_token': create_access_token(id),
                'msg': 'login success'
            }
        else:
            return Response('', 401)
