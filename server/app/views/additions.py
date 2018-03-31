from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.user import UserModel
from app.models.eye import EyeModel


class CheerRank(Resource):
    @jwt_required
    def get(self):
        return [{
            'nickname': user.nickname,
            'tissue_count': user.tissue_count
        } for user in UserModel.objects.order_by('tissue_count')], 200


class PopularEye(Resource):
    @jwt_required
    def get(self):
        eyes = EyeModel.objects

        return [{
            'title': eye.title,
            'category': eye.category,
            'author': eye.author.nickname,
            'posting_time': eye.posting_time,
            'comment_count': eye.comment_count,
            'tear_count': eye.tear_count
        } for eye in eyes if eyes.tear_count >= 3], 200
