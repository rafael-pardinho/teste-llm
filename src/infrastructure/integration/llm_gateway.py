import google.generativeai as genai
from src.domain.interfaces import LLMGatewayInterface

class GeminiLLMGateway(LLMGatewayInterface):
    def __init__(self, api_key: str, model_name: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text if response.text else "Resposta do modelo vazia."
        except Exception as e:
            print(f"Erro ao chamar o modelo Gemini: {e}")
            return "Erro ao obter resposta do modelo."