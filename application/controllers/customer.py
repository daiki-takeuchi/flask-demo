from flask import Blueprint
from flask import render_template

from application.domain.customer import Customer

app = Blueprint('customer', __name__)


@app.route('/', methods=['GET'])
def index():
    result = Customer.query.all()
    return render_template('customer/index.html', result=result)


@app.route('/detail/<customer_id>', methods=['GET'])
def detail(customer_id):
    # customer = Customer.query.filter(Customer.id == customer_id).one()
    customer = Customer.query.filter('customer.id = ' + customer_id).one()
    return render_template('customer/detail.html', customer=customer)
