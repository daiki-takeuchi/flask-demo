from flask import Blueprint
from flask import render_template

from application.service.customer_service import CustomerService

bp = Blueprint('customer', __name__, url_prefix='/customer')
service = CustomerService()


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/index/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    result = service.find_all(page).items
    return render_template('customer/index.html', result=result)


@bp.route('/detail/<customer_id>', methods=['GET'])
def detail(customer_id):
    customer = service.find_by_id(customer_id)
    return render_template('customer/detail.html', customer=customer)
