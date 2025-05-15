from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class ChatLogModel(Base):
    __tablename__ = "chat_logs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False)
    prompt = Column(String, nullable=False)
    response = Column(String)
    model = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())