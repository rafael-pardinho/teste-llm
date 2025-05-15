from sqlalchemy.orm import Session
from src.domain.entities import ChatLog
from src.domain.interfaces import ChatRepositoryInterface
from src.infrastructure.database.models import ChatLogModel
from typing import Optional, List

class ChatRepository(ChatRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def create(self, chat_log: ChatLog) -> ChatLog:
        db_log = ChatLogModel(**chat_log.__dict__)
        self.db.add(db_log)
        self.db.commit()
        self.db.refresh(db_log)
        return ChatLog(
            id=db_log.id,
            user_id=db_log.user_id,
            prompt=db_log.prompt,
            response=db_log.response,
            model=db_log.model,
            timestamp=db_log.timestamp
        )

    def update(self, chat_log: ChatLog) -> ChatLog:
        db_log = self.db.query(ChatLogModel).filter(ChatLogModel.id == chat_log.id).first()
        if db_log:
            db_log.user_id = chat_log.user_id
            db_log.prompt = chat_log.prompt
            db_log.response = chat_log.response
            db_log.model = chat_log.model
            self.db.commit()
            self.db.refresh(db_log)
            return ChatLog(
                id=db_log.id,
                user_id=db_log.user_id,
                prompt=db_log.prompt,
                response=db_log.response,
                model=db_log.model,
                timestamp=db_log.timestamp
            )
        return chat_log

    def get_by_id(self, chat_log_id: str) -> Optional[ChatLog]:
        db_log = self.db.query(ChatLogModel).filter(ChatLogModel.id == chat_log_id).first()
        if db_log:
            return ChatLog(
                id=db_log.id,
                user_id=db_log.user_id,
                prompt=db_log.prompt,
                response=db_log.response,
                model=db_log.model,
                timestamp=db_log.timestamp
            )
        return None

    def get_by_user_id(self, user_id: str) -> List[ChatLog]:
        db_logs = self.db.query(ChatLogModel).filter(ChatLogModel.user_id == user_id).order_by(ChatLogModel.timestamp.desc()).all()
        return [
            ChatLog(
                id=log.id,
                user_id=log.user_id,
                prompt=log.prompt,
                response=log.response,
                model=log.model,
                timestamp=log.timestamp
            )
            for log in db_logs
        ]

    def get_all(self) -> List[ChatLog]:
        db_logs = self.db.query(ChatLogModel).order_by(ChatLogModel.timestamp.desc()).all()
        return [
            ChatLog(
                id=log.id,
                user_id=log.user_id,
                prompt=log.prompt,
                response=log.response,
                model=log.model,
                timestamp=log.timestamp
            )
            for log in db_logs
        ]