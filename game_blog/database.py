from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from security_keys import DB_SETTINGS

cre_string = ('postgresql+psycopg2://' + DB_SETTINGS['ADMIN'] + ':' + DB_SETTINGS['PASSWORD'] + '@' + DB_SETTINGS['HOST']
              + ':' + DB_SETTINGS['PORT'] + '/' + DB_SETTINGS['DB_NAME'])

engine = create_engine(
    cre_string
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
