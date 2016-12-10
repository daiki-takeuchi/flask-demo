import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

from application.blueprint import register
from application.viewhelper import my_filter

pymysql.install_as_MySQLdb()


app = Flask(__name__, template_folder='../templates', static_folder='../static')

config_name = os.getenv('FLASK_CONFIGURATION', 'local')
app.config.from_object('config.' + config_name)

db = SQLAlchemy(app)

register(app)
my_filter(app)


@app.route('/')
def hello_world():
    app.logger.debug('Hello World!')
    return 'Hello World!'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
