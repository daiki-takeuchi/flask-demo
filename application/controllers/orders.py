from flask import Blueprint
from flask import render_template

from application.domain.orders_repository import OrdersRepository

app = Blueprint('orders', __name__)
repository = OrdersRepository()


@app.route('/')
def index():
    result = repository.find_all()
    return render_template('orders/index.html', result=result)


@app.route('/detail/<orders_id>')
def detail(orders_id):
    order = repository.find_by_id(orders_id)
    return render_template('orders/detail.html', order=order)
