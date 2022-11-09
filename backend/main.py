from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from backend.api import api_router
from backend.db import metadata, engine, database
from backend.models import User

app = FastAPI()

metadata.create_all(engine)
app.state.database = database

origins = ["*"]


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
