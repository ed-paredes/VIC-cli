from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    URI_REPOSITORY: str =  Field(..., env="URI_REPOSITORY")
    DATASET_PAHT: str = '/etc/dataset/'
    URL_VACCINATION_CSV: str = 'https://analisi.transparenciacatalunya.cat/api/views/irki-p3c7/rows.csv'
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
settings = Settings()




