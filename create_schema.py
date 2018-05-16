from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    language = Column(String)

    def __repr__(self):
        return "Author(%r)" % (self.fullname)


engine = create_engine('sqlite:///:authors.db:', echo=True)
Base.metadata.create_all(engine)
