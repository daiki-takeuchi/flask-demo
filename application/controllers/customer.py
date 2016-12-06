from flask import Blueprint
from flask import render_template

from application.domain.customer_repository import CustomerRepository

bp = Blueprint('customer', __name__, url_prefix='/customer')
repository = CustomerRepository()


@bp.route('/', methods=['GET'])
def index():
    result = repository.find_all()
    return render_template('customer/index.html', result=result)


@bp.route('/detail/<customer_id>', methods=['GET'])
def detail(customer_id):
    customer = repository.find_by_id(customer_id)
    return render_template('customer/detail.html', customer=customer)
