from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


from app.models.user import UserModel
from app.models.eye import EyeModel


class Signup(Resource):
    def post(self):
        id = request.form['id']
        pw = request.form['pw']
        email = request.form['email']

        if UserModel.objects(id=id):
            return Response('id duplicate', 204)

        UserModel(id=id, pw=pw, email=email).save()

        return Response('signup success', 201)


class Login(Resource):
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


class MyPage(Resource):
    @jwt_required
    def post(self):
        user = UserModel.objects(id=get_jwt_identity()).first()

        if not user:
            return Response('user not founds', 401)

        nickname = request.form['nickname']
        introduction = request.form['introduction']
        # profile_image = request.form['profile_image']

        user.update(nickname=nickname, introduction=introduction)

        return Response('', 201)

    @jwt_required
    def get(self):
        user = UserModel.objects(id=get_jwt_identity()).first()

        if not user:
            return Response('user not founds', 401)

        return {
            'nickname': user.nickname,
            'introduction': user.introduction,
            'eyes': [{
                'title': eye.title,
                'comment_count': eye.comment_count,
                'tear_count': eye.tear_count
            } for eye in EyeModel.objects(author=user)],
            'tissue_count': user.tissue_count,
            'get_tears_count': user.get_tears_count
        }, 200
