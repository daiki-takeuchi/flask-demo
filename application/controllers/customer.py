from flask import Blueprint
from flask import render_template

from application.service.customer_service import CustomerService

bp = Blueprint('customer', __name__, url_prefix='/customer')
service = CustomerService()


@bp.route('/', methods=['GET'])
def index():
    result = service.find_all(1, 10)
    return render_template('customer/index.html', result=result)


@bp.route('/detail/<customer_id>', methods=['GET'])
def detail(customer_id):
    customer = service.find_by_id(customer_id)
    return render_template('customer/detail.html', customer=customer)
