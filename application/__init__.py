import os

from flask import Flask
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import pymysql

from application.blueprint import register

pymysql.install_as_MySQLdb()


app = Flask(__name__, template_folder='../templates', static_folder='../static')

config_name = os.getenv('FLASK_CONFIGURATION', 'local')
app.config.from_object('config.' + config_name)


engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], encoding='utf-8')
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Model = declarative_base()
Model.query = db_session.query_property()

register(app)


@app.route('/')
def hello_world():
    app.logger.debug('Hello World!')
    return 'Hello World!'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def init_db():
    metadata.create_all(bind=engine)
