from datetime import datetime
from typing import Optional
import uuid

class ChatLog:
    def __init__(self, user_id: str, prompt: str, response: Optional[str] = None, model: Optional[str] = None, timestamp: Optional[datetime] = None, id: Optional[str] = None):
        self.id = id if id else str(uuid.uuid4())
        self.user_id = user_id
        self.prompt = prompt
        self.response = response
        self.model = model
        self.timestamp = timestamp if timestamp else datetime.now()