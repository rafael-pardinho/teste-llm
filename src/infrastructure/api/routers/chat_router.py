from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from src.application.dtos import ChatRequest, ChatResponse, ChatLogListResponse
from src.application.services.chat_service import ChatService
from src.infrastructure.api.dependencies import get_chat_service

router = APIRouter()

@router.post("/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, chat_service: ChatService = Depends(get_chat_service)):
    try:
        chat_log = chat_service.process_chat(request.user_id, request.prompt)
        return ChatResponse(**chat_log.__dict__)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a requisição: {str(e)}")

@router.get("/v1/chat/logs", response_model=ChatLogListResponse)
async def get_all_logs(chat_service: ChatService = Depends(get_chat_service)):
    try:
        logs = chat_service.get_all_chat_logs()
        # Converta cada objeto ChatLog para ChatResponse
        response_logs = [ChatResponse(**log.__dict__) for log in logs]
        return ChatLogListResponse(logs=response_logs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar todos os logs: {str(e)}")

@router.get("/v1/chat/{user_id}/logs", response_model=ChatLogListResponse)
async def get_logs_by_user(user_id: str = Path(..., title="The ID of the user to get logs for"), chat_service: ChatService = Depends(get_chat_service)):
    try:
        logs = chat_service.get_chat_logs_by_user(user_id)
        # Converta cada objeto ChatLog para ChatResponse
        response_logs = [ChatResponse(**log.__dict__) for log in logs]
        return ChatLogListResponse(logs=response_logs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar os logs do usuário {user_id}: {str(e)}")