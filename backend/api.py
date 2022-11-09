import aiofiles
from fastapi import APIRouter, HTTPException, UploadFile, File
from uuid import uuid4

from starlette.responses import StreamingResponse

from backend.models import User, Comment
from backend.schemas import CommentBase

api_router = APIRouter(prefix='/api')


@api_router.get("/user/{user_id}")
async def get_user(user_id: int):
    await User.objects.create(first_name='Лысый', last_name='Дед', photo='backend/photos/1.jpg')
    user = await User.objects.select_related(['comments']).get_or_none(pk=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        user.photo = f'image/{user_id}'
        return user


@api_router.post('/user/create')
async def create_user(first_name: str, last_name: str, photo: UploadFile = File(...)):
    photo_name = f'backend/photos/{uuid4()}.jpg'
    async with aiofiles.open(photo_name, "wb") as buffer:
        data = await photo.read()
        await buffer.write(data)
    user = await User.objects.create(first_name=first_name, last_name=last_name, photo=photo_name)
    return user


@api_router.get("/image/{user_id}")
async def get_image(user_id: int):
    user = await User.objects.get(pk=user_id)
    photo = open(user.photo, mode="rb")
    return StreamingResponse(photo, media_type="image/jpg")


@api_router.post('/comment/create', response_model=list[CommentBase])
async def create_comment(user_id: int, text: str):
    await Comment.objects.create(user=user_id, text=text)
    comments = await Comment.objects.filter(user__id=user_id).all()
    return comments


@api_router.get('/comment/{user_id}', response_model=list[CommentBase])
async def get_comment(user_id: int):
    user = await User.objects.get_or_none(pk=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        comments = await Comment.objects.filter(user__id=user_id).all()
        return comments
