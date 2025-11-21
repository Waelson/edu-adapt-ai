# llm_client.py
from openai import OpenAI
from typing import Any, Dict, List
from config import config


class ChatGPTClient:
    """
    Cliente simples para chamadas ao ChatGPT via API oficial.
    Compatível com CrewAI Tools.
    """

    def __init__(self):
        if not config.openai_api_key:
            raise ValueError("OPENAI_API_KEY não definido no .env")
        
        self.client = OpenAI(api_key=config.openai_api_key)
        self.model = config.chat_model
        self.embed_model = config.embedding_model

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.4,
        max_tokens: int | None = None,
    ) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return response.choices[0].message.content or ""

    def embedding(self, text: str) -> List[float]:
        response = self.client.embeddings.create(
            model=self.embed_model,
            input=text,
        )
        return response.data[0].embedding
