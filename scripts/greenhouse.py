import requests
import pandas as pd
from datetime import datetime
import os

def coletar_greenhouse(empresa_slug: str):
    """
    Coleta vagas abertas de uma empresa no Greenhouse.
    
    Parâmetro:
        empresa_slug (str): o identificador da empresa na URL do Greenhouse.
                            Exemplo: 'databricks', 'stripe', 'airbnb', etc.
    """
    base_url = f"https://boards-api.greenhouse.io/v1/boards/{empresa_slug}/jobs"
    response = requests.get(base_url)
    response.raise_for_status()

    jobs = response.json().get("jobs", [])
    if not jobs:
        print(f"Nenhuma vaga encontrada para {empresa_slug}.")
        return

    df = pd.json_normalize(jobs)

    # Criação de diretório se não existir
    os.makedirs("data", exist_ok=True)

    hoje = datetime.today().strftime('%Y-%m-%d')
    nome_arquivo = f"data/greenhouse_{empresa_slug}_{hoje}.parquet"
    df.to_parquet(nome_arquivo, index=False)
    print(f"{len(df)} vagas salvas em {nome_arquivo}.")

if __name__ == "__main__":
    # Exemplo com empresa Databricks
    coletar_greenhouse("databricks")
