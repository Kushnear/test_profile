from pydantic import BaseModel


class UserBase(BaseModel):
    id: int


class CommentBase(BaseModel):
    id: int
    user: UserBase
    text: str
