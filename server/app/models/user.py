from datetime import datetime
from app.models import *


class UserModel(Document):
    meta = {
        'collection': 'user'
    }

    # 회원가입 시 입력
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

    # =======

    # 정보 설정 시 입력
    nickname = StringField(
        required=True,
        default=""
    )

    introduction = StringField(
        max_length=50,
        default=" "
    )

    # profile_image = ImageField()

    # =======

    account_time = DateTimeField(
        default=datetime.now()
    )

    tissue_count = IntField(

    )

    get_tears_count = IntField(

    )
