from fastapi import FastAPI
from src.infrastructure.api.routers import chat_router

app = FastAPI()
app.include_router(chat_router.router)