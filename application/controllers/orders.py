from flask import Blueprint
from flask import abort
from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from application.controllers.form.orders_form import OrdersForm
from application.domain.orders import Orders
from application.service.orders_service import OrdersService

bp = Blueprint('orders', __name__, url_prefix='/orders')
service = OrdersService()


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET', 'POST'])
def index(page=1):
    pagination = service.find_all(page)
    return render_template('orders/index.html', pagination=pagination)


@bp.route('/page/<int:page>', methods=['GET', 'POST'])
def orders_page(page=1):
    return index(page)


@bp.route('/detail/<orders_id>', methods=['GET', 'POST'])
def detail(orders_id=None):
    if orders_id is not None:
        orders = service.find_by_id(orders_id)
    else:
        orders = Orders()
    current_app.logger.debug(str(orders))

    if orders is None and orders_id is not None:
        return abort(404)
    form = OrdersForm(request.form, orders)

    if request.method == 'POST' and form.validate():
        orders.order_number = request.form['order_number']
        orders.order_date = request.form['order_date']
        orders.required_date = request.form['required_date']
        orders.shipped_date = request.form['shipped_date'] or None
        orders.status = request.form['status'] or None
        orders.comments = request.form['comments'] or None
        orders.customer_number = request.form['customer_number'] or None

        service.save(orders)
        return redirect(url_for('.detail', orders_id=orders.id))
    current_app.logger.debug(form.errors)
    return render_template('orders/detail.html', form=form)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    return detail()


@bp.route('/delete/<orders_id>', methods=['GET'])
def delete(orders_id):
    orders = service.find_by_id(orders_id)
    if orders is None:
        return redirect('/orders')
    service.destroy(orders)
    return redirect('/orders')
