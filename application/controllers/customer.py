from flask import Blueprint
from flask import render_template

from application.service.customer_service import CustomerService

bp = Blueprint('customer', __name__, url_prefix='/customer')
service = CustomerService()


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET', 'POST'])
def index(page=1):
    pagination = service.find_all(page)
    return render_template('customer/index.html', pagination=pagination)


@bp.route('/page/<int:page>', methods=['GET', 'POST'])
def customer_page(page=1):
    return index(page)


@bp.route('/detail/<customer_id>', methods=['GET'])
def detail(customer_id):
    customer = service.find_by_id(customer_id)
    return render_template('customer/detail.html', customer=customer)
