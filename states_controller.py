from sqlalchemy import create_engine
from schema import State
from sqlalchemy.orm import sessionmaker
from schema import Base, engine


def create_new_york():
    Session = sessionmaker(bind=engine)
    session = Session()
    # complete the query here

def create_wyoming():
    pass

def query_all_states():
    pass

# def create_cali():
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     cali = State(name="California", capital_city="Sacramento", population=40000000, landlocked=False)
#     session.add(cali)
#     session.commit()

def update_cali():
    pass

# def create_connecticut():
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     ct = State(name="Connecticut", capital_city="Hartford", population=3600000, landlocked=False)
#     session.add(ct)
#     session.commit()

def delete_connecticut():
    pass

# def rollback_session_changes():
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # west_dakota = State(name="West Dakota", capital_city="Fake City", population=123456, landlocked=True)
    # session.add(west_dakota)
