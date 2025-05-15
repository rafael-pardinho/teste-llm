from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime
from src.domain.entities import ChatLog

class ChatRepositoryInterface(ABC):
    @abstractmethod
    def create(self, chat_log: ChatLog) -> ChatLog:
        pass

    @abstractmethod
    def update(self, chat_log: ChatLog) -> ChatLog:
        pass

    @abstractmethod
    def get_by_id(self, chat_log_id: str) -> Optional[ChatLog]:
        pass

class LLMGatewayInterface(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass