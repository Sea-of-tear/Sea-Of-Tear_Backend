from datetime import datetime
from app.models import *


class UserModel(Document):
    meta = {
        'collection': 'user'
    }

    id = StringField(
        required=True,
        primary_key=True
    )

    pw = StringField(
        required=True
    )

    email = StringField(
        required=True
    )

    nickname = StringField(
        required=True,
        default=""
    )

    introduction = StringField(
        max_length=50,
        default=" "
    )

    account_time = DateTimeField(
        default=datetime.now()
    )

    tissue_count = IntField(

    )

    tears_count = IntField(

    )
