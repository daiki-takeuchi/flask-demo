from sqlalchemy import create_engine, MetaData

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import pymysql
pymysql.install_as_MySQLdb()

HOST = '104.198.126.171'
PORT = '3306'
USER = 'test_user'
PASSWORD = 'test_user'
DATABASE = 'sample_db'
SQLALCHEMY_DATABASE_URI = 'mysql://' + USER + ':' + PASSWORD + '@' + HOST + ':' + PORT + '/' + DATABASE

engine = create_engine(SQLALCHEMY_DATABASE_URI, encoding='utf-8')
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Model = declarative_base()
Model.query = db_session.query_property()


def init_db():
    metadata.create_all(bind=engine)