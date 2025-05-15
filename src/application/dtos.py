from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ChatRequest(BaseModel):
    user_id: str
    prompt: str

class ChatResponse(BaseModel):
    id: str
    user_id: str
    prompt: str
    response: Optional[str] = None
    model: str
    timestamp: datetime

class ChatLogListResponse(BaseModel):
    logs: List[ChatResponse]