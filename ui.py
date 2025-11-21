import streamlit as st
from crew.crew_runner import create_crew
import os
import glob
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "crew"))
sys.path.append(os.path.join(BASE_DIR, "tools"))

st.set_page_config(page_title="Adaptador Educacional - IA", layout="wide")

st.title("📘 Adaptador de Conteúdo Educacional")
st.markdown("Adapte textos, gere exemplos, atividades e exporte como PDF usando seu pipeline CrewAI.")

with st.form("form"):
    conteudo = st.text_area("✏️ Conteúdo original", height=200)

    nivel = st.selectbox(
        "🎯 Nível",
        ["iniciante", "intermediário", "avançado"]
    )

    faixa = st.text_input("👶 Faixa etária (ex: 11-13 anos)", "11-13 anos")

    contexto = st.text_input("🏫 Contexto educacional", "alunos do ensino fundamental")

    enviar = st.form_submit_button("🚀 Adaptar conteúdo")

if enviar:
    if not conteudo.strip():
        st.error("Por favor, informe o conteúdo original!")
    else:
        st.info("⏳ Executando o agente… aguarde alguns segundos...")

        crew = create_crew()

        resultado = crew.kickoff(
            inputs={
                "conteudo": conteudo,
                "nivel": nivel,
                "faixa_etaria": faixa,
                "contexto": contexto,
            }
        )

        st.success("✅ Material gerado com sucesso!")

        st.subheader("📄 Resultado Final")
        st.markdown(resultado)

        # Procurar arquivos gerados
        md_files = sorted(glob.glob("output/*.md"), key=os.path.getmtime, reverse=True)
        pdf_files = sorted(glob.glob("output/*.pdf"), key=os.path.getmtime, reverse=True)

        if md_files:
            with open(md_files[0], "r", encoding="utf-8") as f:
                st.download_button("📥 Baixar Markdown", f, file_name=os.path.basename(md_files[0]))

        if pdf_files:
            with open(pdf_files[0], "rb") as f:
                st.download_button("📥 Baixar PDF", f, file_name=os.path.basename(pdf_files[0]))
