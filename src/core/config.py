from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    URI_REPOSITORY: str = "postgresql://postgres:password@db:5432/dev"
    DATASET_PAHT: str = '/etc/dataset/'
    URL_VACCINATION_CSV: str = 'https://analisi.transparenciacatalunya.cat/api/views/irki-p3c7/rows.csv'
settings = Settings()




