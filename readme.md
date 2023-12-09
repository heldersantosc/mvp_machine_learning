# Iniciando Projeto Flask com Virtual Environment

Este é um guia passo a passo para iniciar um projeto Flask usando uma virtual environment.

## Pré-requisitos

- Python 3.x instalado na sua máquina.

## Passos:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/heldersantosc/mvp_machine_learning.git
   cd mvp_machine_learning

2. **Crie uma Virtual Environment:**
    ```bash
    # Windows
    python -m venv .venv

    # Linux/Mac
    python3 -m venv .venv

3. **Ative a Virtual Environment:**
    ```bash
    # Windows
    .venv\Scripts\activate

    # Linux/Mac
    source .venv/bin/activate

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt