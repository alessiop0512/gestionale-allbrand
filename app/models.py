from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DailyMetric(Base):
    __tablename__ = "daily_metrics"

    id = Column(Integer, primary_key=True, index=True)
    store = Column(String)
    date = Column(Date)
    ingressi = Column(Integer)
    pezzi = Column(Integer)
    scontrini = Column(Integer)
    incasso = Column(Float)
    contanti = Column(Float)
    pos = Column(Float)
