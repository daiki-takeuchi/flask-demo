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

    if form.validate_on_submit():
        orders.order_number = form.order_number.data
        orders.order_date = form.order_date.data
        orders.required_date = form.required_date.data
        orders.shipped_date = form.shipped_date.data or None
        orders.status = form.status.data or None
        orders.comments = form.comments.data or None
        orders.customer_number = form.customer_number.data or None

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
