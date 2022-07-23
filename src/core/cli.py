import argparse
import logging
import traceback
from datetime import datetime, timedelta
from typing import List

import pandas as pd
from src.core import utils
from src.models.vaccination import VaccinationBase

from . import repository

TIME_FORMAT = '%d/%m/%Y'

def check_dates_to_update(date: datetime) -> List:
    logging.debug(f'Checking last updated date')
    date_list = []
    last_vaccination = repository.vaccination.get_last_vaccination_date()
    if last_vaccination:
        logging.info(f'Last vaccination was on {last_vaccination}')
        date_list = pd.date_range(start=last_vaccination, end=date, inclusive='right').to_list()

    return date_list


def get_daily_information(vaccination_csv: str, previous_days: int=None)-> pd.DataFrame:
    df = pd.read_csv(vaccination_csv, sep=',')
    df['DATA'] = pd.to_datetime(df['DATA'], format=TIME_FORMAT)    
    now = datetime.now() - timedelta(days=previous_days)
    
    dates_to_update = check_dates_to_update(now)
    if not dates_to_update:
        logging.info(f'Could not found any previous register')
        start_date = df['DATA'].agg('min')
        logging.info(f'Dates to update: from {start_date} to {now}')
        dates_to_update = df.loc[(df['DATA'] > start_date) & (df['DATA'] < now) ]['DATA']
        
    df = df.loc[(df['DOSI'] == 1) &  (df['DATA'].isin(dates_to_update))]
    if df.empty:
        logging.warning(f'Could not found new registers to update')
        exit(0)
    df = df.groupby(['COMARCA', 'DATA']).agg('sum')
    df = df.reset_index()
    logging.info(f'Information to update [ {len(df)} ]')
    return df


def main():
    args = parse_args()
    previous_days  = args.get('previous_days')
    level = args.get('log_level')
    __set_log_level(level)
    try:
        vaccination_csv = utils.get_vaccination_csv()
        df_vac = get_daily_information(vaccination_csv, previous_days=previous_days)
        vaccination_to_update = df_vac.apply(lambda row: VaccinationBase.create_vaccination_model(row), axis=1).tolist()
        repository.vaccination.insert(vaccination_information=vaccination_to_update)
    except Exception as e:
        print(traceback.print_exc())
        logging.warning(f'Something went wrong, [{e}]')

def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--previous_days',type=int, default=1, help='Days before the process')
    arg_parser.add_argument('--log-level',type=str, default='INFO', help='Provide logging leve')
    
    args, _ = arg_parser.parse_known_args()
    args_dict = vars(args)
    if not args:
        arg_parser.print_help()
        exit(1)
    return args_dict

def __set_log_level(level: str):
    level = logging.getLevelName(level=level)
    logging.basicConfig(level=level)
