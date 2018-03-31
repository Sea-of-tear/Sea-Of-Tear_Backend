from app.models import *
from app.models.user import UserModel


class Comment(EmbeddedDocument):
    author = ReferenceField(
        document_type=UserModel,
        required=True
    )

    description = StringField(required=True, default=" ")

    tissue = BooleanField(
        default=False
    )


class Eye(Document):
    title = StringField(required=True, max_length=25)
    description = StringField(required=True)
    author = ReferenceField(
        document_type=UserModel,
        required=True
    )

    background_image = ImageField(required=True)
    category = IntField(required=True)

    comments = ListField(
        EmbeddedDocumentField(
            document_type=Comment,
            required=True
        )
    )

    comment_count = IntField()
    tear_count = IntField()
