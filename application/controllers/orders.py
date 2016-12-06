from flask import Blueprint
from flask import render_template

from application.domain.orders_repository import OrdersRepository

bp = Blueprint('orders', __name__, url_prefix='/orders')
repository = OrdersRepository()


@bp.route('/')
def index():
    result = repository.find_all()
    return render_template('orders/index.html', result=result)


@bp.route('/detail/<orders_id>')
def detail(orders_id):
    order = repository.find_by_id(orders_id)
    return render_template('orders/detail.html', order=order)
