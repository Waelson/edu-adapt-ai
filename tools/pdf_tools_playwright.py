# tools/pdf_tools_playwright.py

import os
from markdown import markdown
from crewai.tools import tool
from playwright.sync_api import sync_playwright
from datetime import datetime


class PDFTools:

    @staticmethod
    def _ts():
        return datetime.now().strftime("%Y%m%d-%H%M%S")

    @staticmethod
    @tool("Gerar PDF com estilo a partir de markdown")
    def gerar_pdf(conteudo_md: str, nome_base: str = "material") -> str:
        """Gera um arquivo PDF estilizado a partir de conteúdo Markdown."""

        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        nome = f"{nome_base}-{PDFTools._ts()}.pdf"
        caminho_pdf = os.path.join(output_dir, nome)

        # Converte markdown para HTML estilizado
        html = markdown(conteudo_md, extensions=["fenced_code", "tables"])

        html_com_css = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    line-height: 1.6;
                    color: #222;
                }}
                h1, h2, h3 {{
                    color: #111;
                    margin-top: 24px;
                }}
                pre {{
                    background: #f4f4f4;
                    padding: 12px;
                    border-left: 4px solid #888;
                    overflow-x: auto;
                }}
                code {{
                    background: #f4f4f4;
                    padding: 3px 6px;
                    border-radius: 4px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                }}
                th {{
                    background: #ddd;
                }}
                ul, ol {{
                    margin: 12px 0;
                }}
            </style>
        </head>
        <body>
            {html}
        </body>
        </html>
        """

        # Gera o PDF com Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_content(html_com_css)
            page.pdf(path=caminho_pdf, format="A4")
            browser.close()

        return caminho_pdf
