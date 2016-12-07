from flask import Blueprint
from flask import render_template

from application.service.payment_service import PaymentService

bp = Blueprint('payment', __name__, url_prefix='/payment')
service = PaymentService()


@bp.route('/')
def index():
    result = service.find_all(1, 10)
    return render_template('payment/index.html', result=result)


@bp.route('/detail/<payment_id>')
def detail(payment_id):
    payment = service.find_by_id(payment_id)
    return render_template('payment/detail.html', payment=payment)
