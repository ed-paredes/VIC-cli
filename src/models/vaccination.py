
from datetime import datetime
from pydantic import BaseModel


class VaccinationBase(BaseModel):
    comarca: str
    vaccination_date: datetime
    doses: int
    manufacturer: str
    last_updated: datetime