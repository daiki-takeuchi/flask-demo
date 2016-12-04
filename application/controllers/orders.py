from flask import Blueprint
from flask import render_template

from application.domain.orders import Orders

app = Blueprint('orders', __name__)


@app.route('/')
def index():
    result = Orders.query.all()
    return render_template('orders/index.html', result=result)


@app.route('/detail/<orders_id>')
def detail(orders_id):
    order = Orders.query.filter('orders.id = ' + orders_id).one()
    return render_template('orders/detail.html', order=order)
