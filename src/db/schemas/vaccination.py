from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import String, DateTime
from .base import Base



class Vaccination(Base):
    id = Column(Integer, primary_key=True)
    comarca = Column(String, nullable=False)
    vaccination_date = Column(DateTime)
    doses = Column(Integer, nullable=False)
    last_updated = Column(DateTime, nullable=False)