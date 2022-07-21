from sqlalchemy.orm import Session
from .schemas.vaccination import Vaccination

class VaccinationRepository(object):
    def __init__(self, db: Session,  schema:Vaccination) -> None:
        self.db = db
        self.schema = schema
    
    def insert(self):
        pass


    def get_last_vaccination_date(self):
        last_vaccination_date = self.db.query(self.schema.vaccination_date).order_by(self.schema.vaccination_date).scalar()
        return last_vaccination_date 