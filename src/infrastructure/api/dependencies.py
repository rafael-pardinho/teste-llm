from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.infrastructure.database.models import Base
from src.infrastructure.database.repositories import ChatRepository
from src.infrastructure.integration.llm_gateway import GeminiLLMGateway
from src.application.ports.chat_repository import ChatRepositoryPort
from src.application.services.chat_service import ChatService
from fastapi import Depends
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://userllm:passllm@db:5432/llm_db")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_NAME = os.environ.get("MODEL_NAME", "gemini-2.0-flash")

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_chat_repository(db: Session = Depends(get_db)):
    return ChatRepositoryPort(ChatRepository(db))

def get_llm_gateway():
    if not GEMINI_API_KEY:
        raise ValueError("A chave da API Gemini não foi configurada.")
    return GeminiLLMGateway(api_key=GEMINI_API_KEY, model_name=MODEL_NAME)

def get_chat_service(chat_repository: ChatRepositoryPort = Depends(get_chat_repository), llm_gateway: GeminiLLMGateway = Depends(get_llm_gateway)):
    return ChatService(chat_repository, llm_gateway, MODEL_NAME)