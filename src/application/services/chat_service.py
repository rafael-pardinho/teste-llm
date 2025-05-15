from src.domain.entities import ChatLog
from src.application.ports.chat_repository import ChatRepositoryPort
from src.domain.interfaces import LLMGatewayInterface
from typing import List

class ChatService:
    def __init__(self, chat_repository: ChatRepositoryPort, llm_gateway: LLMGatewayInterface, model_name: str):
        self.chat_repository = chat_repository
        self.llm_gateway = llm_gateway
        self.model_name = model_name

    def process_chat(self, user_id: str, prompt: str) -> ChatLog:
        chat_log = ChatLog(user_id=user_id, prompt=prompt)
        self.chat_repository.create(chat_log)

        llm_response = self.llm_gateway.generate_response(prompt)
        chat_log.response = llm_response
        chat_log.model = self.model_name
        self.chat_repository.update(chat_log)
        return chat_log

    def get_chat_logs_by_user(self, user_id: str) -> List[ChatLog]:
        return self.chat_repository.get_by_user_id(user_id)

    def get_all_chat_logs(self) -> List[ChatLog]:
        return self.chat_repository.get_all()