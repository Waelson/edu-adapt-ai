# crew/agent_content_adaptor.py

from crewai import Agent
from tools.content_tools import ContentTools
from tools.file_tools import FileTools
from tools.pdf_tools_playwright import PDFTools


def create_content_agent():
    content_tools = ContentTools()
    file_tools = FileTools()
    pdf_tools = PDFTools()

    return Agent(
        name="Agente Adaptador de Conteúdo",
        role="Especialista em adaptação pedagógica e criação de materiais educacionais",
        goal="Transformar conteúdo bruto em versões adaptadas por nível, gerar exemplos, atividades e arquivos finais.",
        backstory=(
            "Você é um agente de IA treinado para auxiliar professores, escolas e instituições "
            "a adaptar conteúdos para diferentes níveis de complexidade, faixas etárias e estilos "
            "de aprendizagem. Seu trabalho é garantir clareza, precisão pedagógica e que o material "
            "final seja útil e pronto para uso em sala de aula."
        ),
        tools=[
            content_tools.simplificar_texto,
            content_tools.expandir_avancado,
            content_tools.adaptar_vocabulario,
            content_tools.gerar_exemplos,
            content_tools.gerar_atividades,
            content_tools.validar,
            file_tools.gerar_md,
            file_tools.md_para_html,
            pdf_tools.gerar_pdf,
        ],
        llm="gpt-4.1-mini",
        verbose=True,
    )
