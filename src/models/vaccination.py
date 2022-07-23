
from datetime import datetime
from pandas import Series
from pydantic import BaseModel


class VaccinationBase(BaseModel):
    comarca: str
    vaccination_date: datetime
    doses: int
    last_updated: datetime

    @staticmethod
    def create_vaccination_model(row: Series) -> 'VaccinationBase':
        return VaccinationBase(
            comarca = row['COMARCA'], 
            vaccination_date = row['DATA'],
            doses = row['DOSI'],
            last_updated = datetime.now()
        )
