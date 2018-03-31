from datetime import datetime
from bson.objectid import ObjectId

from app.models import *
from app.models.user import UserModel


class Comment(EmbeddedDocument):
    id = ObjectIdField(primary_key=True, default=ObjectId())
    # EmbeddedDocument 는 식별자가 없어서 직접 설정

    author = ReferenceField(
        document_type=UserModel,
        required=True
    )

    description = StringField(required=True, default=" ")

    tissue = BooleanField(
        default=False
    )


class EyeModel(Document):
    title = StringField(required=True, max_length=25)
    description = StringField(required=True)
    author = ReferenceField(
        document_type=UserModel,
        required=True
    )

    # background_image = ImageField(required=True)
    category = IntField(required=True)

    comments = ListField(
        EmbeddedDocumentField(
            document_type=Comment
        )
    )

    posting_time = DateTimeField(
        default=datetime.now()
    )

    comment_count = IntField(default=0)
    tear_count = IntField(default=0)
