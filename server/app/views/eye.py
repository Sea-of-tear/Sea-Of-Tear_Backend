from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.user import UserModel
from app.models.eye import EyeModel


class PostEye(Resource):
    @jwt_required
    def post(self):
        user = UserModel.objects(id=get_jwt_identity()).first()

        if not user:
            return Response('', 401)

        title = request.form['title']
        description = request.form['description']
        background_image = request.files['background']
        category = request.form['category']

        EyeModel(
            title=title,
            description=description,
            author=user,
            background_image=background_image,
            category=category
        ).save()

        return Response('', 201)
