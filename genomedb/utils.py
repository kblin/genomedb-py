# vim: set fileencoding=utf-8 :

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genomedb.models import Base

def init_database(options):
    """Initialise the database and retun a session"""
    engine = create_engine(options.db)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return Session()
