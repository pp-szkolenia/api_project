from sqlalchemy import Column, Integer, Boolean, String, Double

from src.db.orm import Base


class CarsTable(Base):
    __tablename__ = "cars"

    price = Column('price', Double, nullable = True )
    currency  = Column('currency', String, nullable = True)
    brand  = Column('brand', String, nullable = True)
    body = Column('body', String, nullable = True)
    engine_vol = Column('engine_vol', Double, nullable = True)
    fuel = Column('fuel', String, nullable = True)
    drive = Column('drive', String, nullable = True)
    power = Column('power', Double, nullable = True)
    gearbox_is_manual = Column('gearbox_is_manual', String, nullable = True)
    prod_year = Column('prod_year', Integer, nullable = False)
    orig_country = Column('orig_country', String , nullable = True)
    mileage = Column('mileage', Double , nullable = True)
    color = Column('color', String , nullable = True)
    title = Column('title', String , nullable = True)
    offer_timestamp  = Column('offer_timestamp', String , nullable = True)