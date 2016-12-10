from flask import Blueprint
from flask import render_template

from application.service.orders_service import OrdersService

bp = Blueprint('orders', __name__, url_prefix='/orders')
service = OrdersService()


@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/index/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    result = service.find_all(page).items
    return render_template('orders/index.html', result=result)


@bp.route('/detail/<orders_id>')
def detail(orders_id):
    order = service.find_by_id(orders_id)
    return render_template('orders/detail.html', order=order)
