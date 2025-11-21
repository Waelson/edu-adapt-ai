# config.py
import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Carrega o arquivo .env automaticamente
load_dotenv()

@dataclass
class AppConfig:
    openai_api_key: str
    chat_model: str
    embedding_model: str

    @classmethod
    def load(cls):
        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY", ""),
            chat_model=os.getenv("CHAT_MODEL", "gpt-4.1-mini"),
            embedding_model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        )

config = AppConfig.load()
