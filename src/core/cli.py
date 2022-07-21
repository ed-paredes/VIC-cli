import argparse
from datetime import datetime, timedelta
from typing import List
from  src.core import utils
from src.models.vaccination import VaccinationBase
import pandas as pd
from . import repository


def check_dates_to_update(date: datetime) -> list:
    last_vaccination = repository.vaccination.get_last_vaccination_date()
    date_list = pd.date_range(start=last_vaccination, end=date, inclusive='right').to_list()
    return date_list


def get_daily_information(vaccination_csv: str)-> List[VaccinationBase]:
    df = pd.read_csv(vaccination_csv, sep=',')
    now = datetime.now() - timedelta(days=5)
    dates_to_update = check_dates_to_update(now)
    dates_to_update = [ date.strftime("%d/%m/%Y") for date in dates_to_update]
    df = df.loc[(df['DOSI'] == 1) &  (df['DATA'].isin(dates_to_update))]
    df = df.groupby(['COMARCA', 'DATA']).agg('sum')
    df = df.reset_index()
    return df
    


def main(args:dict = None):
    if not args:
        args = parse_args()
    vaccination_csv = utils.get_vaccination_csv()
    df_v = get_daily_information(vaccination_csv)
    
    repository.vaccination.insert()




def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--from-date', metavar='<str>', type=str, default=None,
                       help='Date from get')
    arg_parser.add_argument('--greedy', '-g', action="store_true", default=False,
                       help='Greedy mode, will not exit until there are no more Nodes to process')

    args, _ = arg_parser.parse_known_args()
    args_dict = vars(args)
    if not args:
        arg_parser.print_help()
        exit(1)
    return args_dict

