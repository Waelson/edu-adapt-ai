# Caminho do ambiente virtual
VENV_DIR = venv

.PHONY: venv install deps playwright setup clean run

# Cria o ambiente virtual
venv:
	python -m venv $(VENV_DIR)

# Instala as dependências do projeto
deps:
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

# Instala o Chromium do Playwright
playwright:
	$(VENV_DIR)/bin/playwright install chromium

# Setup completo (venv + deps + playwright)
setup: venv deps playwright
	@echo "✔ Ambiente configurado com sucesso!"

# Limpa ambiente, output e caches Python
clean:
	rm -rf $(VENV_DIR) output
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "🧹 Limpeza completa!"

ui:
	$(VENV_DIR)/bin/streamlit run ui.py	

# Rodar o projeto principal
run:
	$(VENV_DIR)/bin/python main.py
