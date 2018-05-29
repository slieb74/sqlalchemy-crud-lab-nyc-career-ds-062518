from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    # CREATE THE SCHEMA HERE
    pass

engine = create_engine('sqlite:///states.db', echo=True)
Base.metadata.create_all(engine)
