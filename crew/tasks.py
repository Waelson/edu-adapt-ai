from crewai import Task
import os

def create_tasks(agent):

    return [

        # 1) ADAPTAR TEXTO
        Task(
            name="Adaptar texto",
            description=(
                "Adapte o conteúdo original conforme o nível solicitado.\n\n"
                "CONTEÚDO ORIGINAL:\n{{conteudo}}\n\n"
                "Nível: {{nivel}}\n"
                "Faixa etária: {{faixa_etaria}}\n"
                "Contexto: {{contexto}}\n\n"
                "Retorne apenas o texto adaptado."
            ),
            expected_output="Texto adaptado.",
            agent=agent,
        ),

        # 2) GERAR EXEMPLOS
        Task(
            name="Gerar exemplos",
            description=(
                "Gere exemplos claros baseados no texto adaptado:\n\n"
                "{{ Adaptar texto.output }}\n\n"
                "Retorne apenas os exemplos."
            ),
            expected_output="Lista de exemplos contextualizados.",
            agent=agent,
            input={"texto_adaptado": "{{ Adaptar texto.output }}"},
        ),

        # 3) GERAR ATIVIDADES
        Task(
            name="Gerar atividades",
            description=(
                "Com base no texto e exemplos abaixo, crie atividades:\n\n"
                "TEXTO ADAPTADO:\n{{ Adaptar texto.output }}\n\n"
                "EXEMPLOS:\n{{ Gerar exemplos.output }}\n\n"
            ),
            expected_output="Lista de atividades pedagógicas.",
            agent=agent,
            input={
                "texto_adaptado": "{{ Adaptar texto.output }}",
                "exemplos": "{{ Gerar exemplos.output }}"
            },
        ),

        # 4) VALIDAR MATERIAL FINAL
        Task(
            name="Validar material final",
            description=(
                "Combine texto, exemplos e atividades:\n\n"
                "- TEXTO:\n{{ Adaptar texto.output }}\n"
                "- EXEMPLOS:\n{{ Gerar exemplos.output }}\n"
                "- ATIVIDADES:\n{{ Gerar atividades.output }}\n\n"
                "Retorne um Markdown único e organizado."
            ),
            expected_output="Markdown final validado.",
            agent=agent,
            input={
                "texto_adaptado": "{{ Adaptar texto.output }}",
                "exemplos": "{{ Gerar exemplos.output }}",
                "atividades": "{{ Gerar atividades.output }}"
            },
        ),

        # 5) GERAR ARQUIVO .MD
        Task(
            name="Gerar Markdown",
            description=(
                "Converta o material final validado em um arquivo Markdown.\n"
                "Use a TOOL 'Gerar arquivo markdown'.\n"
                "Passe como input:\n"
                '{ "conteudo_md": "{{ Validar material final.output }}" }'
            ),
            expected_output="Caminho do arquivo .md gerado.",
            agent=agent,
            use_tools=True,
            input={
                "conteudo_md": "{{ Validar material final.output }}"
            },
        ),

        # 6) LER ARQUIVO .MD
        Task(
            name="Carregar Markdown",
            description=(
                "Leia o conteúdo do arquivo Markdown gerado anteriormente.\n"
                "Arquivo: {{ Gerar Markdown.output }}\n\n"
                "Retorne APENAS o conteúdo do arquivo."
            ),
            expected_output="Conteúdo do arquivo Markdown.",
            agent=agent,
            input={"caminho_md": "{{ Gerar Markdown.output }}"},
        ),

        # 7) GERAR PDF FINAL
        Task(
            name="Gerar PDF",
            description=(
                "Use a TOOL 'Gerar PDF com estilo a partir de markdown'.\n\n"
                "Input da tool deve ser:\n"
                '{ "conteudo_md": "{{ Carregar Markdown.output }}", "nome_base": "material_final" }'
            ),
            expected_output="Caminho do PDF final.",
            agent=agent,
            use_tools=True,
            input={
                "conteudo_md": "{{ Carregar Markdown.output }}",
                "nome_base": "material_final"
            },
        ),
    ]
