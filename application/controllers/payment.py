from flask import Blueprint
from flask import abort
from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from application.controllers.form.payment_form import PaymentForm
from application.domain.payment import Payment
from application.service.payment_service import PaymentService

bp = Blueprint('payment', __name__, url_prefix='/payment')
service = PaymentService()


@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
def index(page=1):
    pagination = service.find_all(page)
    return render_template('payment/index.html', pagination=pagination)


@bp.route('/page/<int:page>', methods=['GET', 'POST'])
def payment_page(page=1):
    return index(page)


@bp.route('/detail/<payment_id>', methods=['GET', 'POST'])
def detail(payment_id=None):
    if payment_id is not None:
        payment = service.find_by_id(payment_id)
    else:
        payment = Payment()
    current_app.logger.debug(str(payment))

    if payment is None and payment_id is not None:
        return abort(404)
    form = PaymentForm(request.form, payment)

    if request.method == 'POST' and form.validate():
        payment.customer_number = request.form['customer_number']
        payment.check_number = request.form['check_number']
        payment.payment_date = request.form['payment_date']
        payment.amount = request.form['amount']

        service.save(payment)
        return redirect(url_for('.detail', payment_id=payment.id))
    current_app.logger.debug(form.errors)
    return render_template('payment/detail.html', form=form)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    return detail()


@bp.route('/delete/<payment_id>', methods=['GET'])
def delete(payment_id):
    orders = service.find_by_id(payment_id)
    if orders is None:
        return redirect('/payment')
    service.destroy(orders)
    return redirect('/payment')
