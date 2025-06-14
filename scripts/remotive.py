import requests
import pandas as pd
from datetime import datetime

def coletar_remotive():
    url = "https://remotive.io/api/remote-jobs"
    response = requests.get(url)
    response.raise_for_status()

    jobs = response.json().get("jobs", [])
    df = pd.DataFrame(jobs)

    hoje = datetime.today().strftime('%Y-%m-%d')
    df.to_parquet(f"data/remotive_jobs_{hoje}.parquet", index=False)
    print(f"{len(df)} vagas salvas com sucesso.")

if __name__ == "__main__":
    coletar_remotive()
