from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital_city = Column(String)
    population = Column(Integer)
    landlocked = Column(Boolean)


engine = create_engine('sqlite:///states.db', echo=True)
Base.metadata.create_all(engine)
