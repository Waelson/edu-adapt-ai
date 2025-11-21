from crew.crew_runner import create_crew

conteudo = """
A fotossíntese é o processo pelo qual as plantas transformam luz em energia química.
"""

nivel = "iniciante"
faixa = "11-13 anos"
contexto = "alunos do ensino fundamental"

crew = create_crew()

resultado = crew.kickoff(
    inputs={
        "conteudo": conteudo,
        "nivel": nivel,
        "faixa_etaria": faixa,
        "contexto": contexto,
    }
)

print("=== RESULTADO FINAL ===")
print(resultado)
