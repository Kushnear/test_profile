import ormar
from typing import Optional, Union, Dict
from backend.db import MainMeta


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: str = ormar.Integer(primary_key=True)
    first_name: str = ormar.String(max_length=100, unique=True)
    last_name: str = ormar.String(max_length=100, unique=True)
    photo: str = ormar.String(max_length=1000)


class Comment(ormar.Model):
    class Meta(MainMeta):
        pass

    id: str = ormar.Integer(primary_key=True)
    user: Union[User, Dict] = ormar.ForeignKey(User)
    text: str = ormar.String(max_length=10000)