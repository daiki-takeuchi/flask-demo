from flask import Blueprint
from flask import render_template

from application.domain.payment_repository import PaymentRepository

bp = Blueprint('payment', __name__, url_prefix='/payment')
repository = PaymentRepository()


@bp.route('/')
def index():
    result = repository.find_all()
    return render_template('payment/index.html', result=result)


@bp.route('/detail/<payment_id>')
def detail(payment_id):
    payment = repository.find_by_id(payment_id)
    return render_template('payment/detail.html', payment=payment)
