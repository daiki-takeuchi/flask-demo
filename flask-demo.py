import os

from flask import Flask

from application.controllers import customer
from application.controllers import orders
from application.controllers import payment
from application.controllers import product
from application.controllers import product_line
from application.database import db_session

app = Flask(__name__)
config_name = os.getenv('FLASK_CONFIGURATION', 'local')
app.config.from_object('config.' + config_name)

app.register_blueprint(customer.bp)
app.register_blueprint(orders.bp)
app.register_blueprint(payment.bp)
app.register_blueprint(product.bp)
app.register_blueprint(product_line.bp)


@app.route('/')
def hello_world():
    # app.logger.debug(app.config['SQLALCHEMY_DATABASE_URI'])
    app.logger.debug('Hello World!')
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.error('An error occurred')
    return 'Hello World!'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
