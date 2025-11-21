# tools/content_tools.py

from crewai.tools import tool
from llm_client import ChatGPTClient

class ContentTools:

    @staticmethod
    @tool("Simplificar texto para nível iniciante")
    def simplificar_texto(conteudo: str, params: dict) -> str:
        """Simplifica um texto para iniciantes."""
        llm = ChatGPTClient()

        prompt = f"""
Reescreva o texto abaixo em nível iniciante.
Parâmetros: {params}

Texto:
{conteudo}
"""
        return llm.chat("Professor especialista", prompt)

    @staticmethod
    @tool("Expandir texto para nível avançado")
    def expandir_avancado(conteudo: str, params: dict) -> str:
        """Expande o texto para nível avançado."""
        llm = ChatGPTClient()

        prompt = f"""
Expanda o conteúdo para nível avançado.

Texto:
{conteudo}
"""
        return llm.chat("Professor universitário", prompt)

    @staticmethod
    @tool("Adaptar vocabulário por faixa etária")
    def adaptar_vocabulario(conteudo: str, params: dict) -> str:
        """Adapta o vocabulário para a faixa etária desejada."""
        llm = ChatGPTClient()

        prompt = f"""
Adapte o vocabulário do texto abaixo.
Parâmetros: {params}

Texto:
{conteudo}
"""
        return llm.chat("Pedagogo especialista", prompt)

    @staticmethod
    @tool("Criar exemplos contextualizados")
    def gerar_exemplos(conteudo: str, params: dict) -> str:
        """Gera exemplos contextualizados de acordo com idade, nível e contexto."""
        llm = ChatGPTClient()

        prompt = f"""
Crie 3–5 exemplos contextualizados.

Texto:
{conteudo}

Parâmetros: {params}
"""
        return llm.chat("Criador de exemplos", prompt)

    @staticmethod
    @tool("Criar atividades pedagógicas")
    def gerar_atividades(conteudo: str, params: dict) -> str:
        """Cria atividades pedagógicas compatíveis com o conteúdo."""
        llm = ChatGPTClient()

        prompt = f"""
Crie atividades pedagógicas (compreensão, prática, reflexão).

Texto:
{conteudo}

Parâmetros: {params}
"""
        return llm.chat("Criador de atividades", prompt)

    @staticmethod
    @tool("Validar pedagogicamente o conteúdo")
    def validar(original: str, adaptado: str, params: dict) -> str:
        """Valida pedagogicamente o conteúdo adaptado."""
        llm = ChatGPTClient()

        prompt = f"""
Valide pedagogicamente a adaptação.

Original:
{original}

Adaptado:
{adaptado}

Parâmetros: {params}
"""
        return llm.chat("Revisor pedagógico", prompt)
