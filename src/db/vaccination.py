import logging
from typing import List
from sqlalchemy.orm import Session
from .schemas.vaccination import Vaccination
from src.models.vaccination import VaccinationBase

class VaccinationRepository(object):
    def __init__(self, db: Session,  schema:Vaccination) -> None:
        self.db = db
        self.schema = schema
    
    def insert(self, vaccination_information: List[VaccinationBase])-> None:
        logging.debug('Inserting vaccination information')
        self.db.bulk_insert_mappings(
            self.schema,
            [
                dict(
                    comarca=vac.comarca,
                    vaccination=vac.doses,
                    doses=vac.doses,
                    vaccination_date=vac.vaccination_date,
                    last_updated=vac.last_updated
                )for vac in vaccination_information
            ]
        )
        self.db.commit()

    def get_last_vaccination_date(self):
        last_vaccination_date = None
        last_vaccination_date = self.db.query(self.schema.vaccination_date).order_by(self.schema.vaccination_date.desc()).first()
        if last_vaccination_date:
            last_vaccination_date = last_vaccination_date._asdict()['vaccination_date']
        return last_vaccination_date