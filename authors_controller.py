from sqlalchemy import *
from create_schema import Author
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///:authors.db:', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

dostoevsky = Author(fullname="Fyodor Dostoevsky", language="Russian")
tolkien = Author(fullname="John Ronald Reuel Tolkien", language="English")

session.add(dostoevsky)
session.add(tolkien)
session.commit()

import pdb; pdb.set_trace()
