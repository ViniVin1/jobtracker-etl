# jobtracker-etl

Projeto de ETL automatizado para coleta, tratamento e análise de dados de vagas de tecnologia via APIs públicas como Remotive e Greenhouse.

## 📐 Arquitetura
A arquitetura segue o padrão em camadas (Raw → Bronze → Silver), utilizando:
- Python para scripts de coleta e tratamento
- Airflow para orquestração
- Docker para empacotamento
- AWS S3 como Data Lake
- PostgreSQL como metastore do Airflow

## 📁 Estrutura

jobtracker-etl/
├── dags/ # DAGs do Airflow
├── scripts/ # Scripts de coleta e tratamento
├── config/ # Configurações e parâmetros
├── docker/ # Dockerfile e Compose
├── data/ # Dados locais para testes
├── .venv/ # Ambiente virtual
├── requirements.txt # Dependências Python
└── README.md