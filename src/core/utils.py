
from datetime import datetime
import logging
import os
from src.core.config import settings
import wget

def get_vaccination_csv() -> str:
    vaccionation_csv = get_vaccination_filename()
    if not os.path.exists(vaccionation_csv):
        logging.info('Downloading vaccination file')
        vaccionation_csv = wget.download(f'{settings.URL_VACCINATION_CSV}', vaccionation_csv)
    return vaccionation_csv


def get_vaccination_filename():
    now = datetime.now() 
    basename = f'vaccinations_{now.strftime("%Y%m%d")}.csv'
    vaccionation_csv = os.path.join(settings.DATASET_PAHT, basename)
    return vaccionation_csv