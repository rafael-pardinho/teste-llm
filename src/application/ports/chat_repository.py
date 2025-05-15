from src.domain.interfaces import ChatRepositoryInterface
from src.domain.entities import ChatLog
from typing import Optional, List

class ChatRepositoryPort(ChatRepositoryInterface):
    def __init__(self, repository):
        self.repository = repository

    def create(self, chat_log: ChatLog) -> ChatLog:
        return self.repository.create(chat_log)

    def update(self, chat_log: ChatLog) -> ChatLog:
        return self.repository.update(chat_log)

    def get_by_id(self, chat_log_id: str) -> Optional[ChatLog]:
        return self.repository.get_by_id(chat_log_id)

    def get_by_user_id(self, user_id: str) -> List[ChatLog]:
        return self.repository.get_by_user_id(user_id)

    def get_all(self) -> List[ChatLog]:
        return self.repository.get_all()