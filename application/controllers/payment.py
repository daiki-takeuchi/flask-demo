from flask import Blueprint
from flask import render_template

from application.service.payment_service import PaymentService

bp = Blueprint('payment', __name__, url_prefix='/payment')
service = PaymentService()


@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/index/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    pagination = service.find_all(page)
    return render_template('payment/index.html', pagination=pagination)


@bp.route('/page/<int:page>', methods=['GET', 'POST'])
def payment_page(page=1):
    return index(page)


@bp.route('/detail/<payment_id>')
def detail(payment_id):
    payment = service.find_by_id(payment_id)
    return render_template('payment/detail.html', payment=payment)
