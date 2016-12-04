from flask import Flask
from application.controllers import customer
from application.controllers import orders
from application.controllers import payment
from application.controllers import product
from application.controllers import product_line

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

app.register_blueprint(customer.app, url_prefix='/customer')
app.register_blueprint(orders.app, url_prefix='/orders')
app.register_blueprint(payment.app, url_prefix='/payment')
app.register_blueprint(product.app, url_prefix='/product')
app.register_blueprint(product_line.app, url_prefix='/productline')

if __name__ == '__main__':
    app.run()

