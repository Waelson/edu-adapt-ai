# tools/file_tools.py

import os
from datetime import datetime
from markdown import markdown
from crewai.tools import tool

class FileTools:

    @staticmethod
    def _ts():
        return datetime.now().strftime("%Y%m%d-%H%M%S")

    @staticmethod
    @tool("Gerar arquivo markdown")
    def gerar_md(conteudo_md: str, nome_base: str = "material") -> str:
        """Gera um arquivo Markdown (.md) com o conteúdo fornecido."""
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        nome = f"{nome_base}-{FileTools._ts()}.md"
        caminho = os.path.join(output_dir, nome)

        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo_md)

        return caminho

    @staticmethod
    @tool("Converter markdown para HTML")
    def md_para_html(conteudo_md: str) -> str:
        """Converte Markdown para HTML renderizável."""
        return markdown(conteudo_md, extensions=["fenced_code", "tables"])
