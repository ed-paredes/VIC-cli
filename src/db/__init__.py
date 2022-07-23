from sqlalchemy.orm import sessionmaker
from src.core.config import settings
from sqlalchemy import create_engine
from src.db.schemas.vaccination import Vaccination
from . import vaccination
from sqlalchemy import *


class Repository(object):

    def __init__(self):
        #  create
        # the tables un-commenting the next line
        meta = MetaData()
        engine = create_engine(settings.URI_REPOSITORY, future=True)
        create_tables(meta)
        meta.create_all(engine)
        self.SessionLocal = sessionmaker(autoflush=True, bind=engine)
        self.vaccination = vaccination.VaccinationRepository(self.SessionLocal(), Vaccination)


def create_tables(meta: MetaData):

    vaccination = Table(
        'vaccination', meta,
        Column('id', Integer, primary_key=True),
        Column('comarca', String, nullable=False),
        Column('vaccination_date', DateTime),
        Column('doses', Integer, nullable=False),
        Column('last_updated', DateTime, nullable=False)
        
    )
    