from flask import Blueprint
from flask import render_template

from application.domain.payment_repository import PaymentRepository

app = Blueprint('payment', __name__)
repository = PaymentRepository()


@app.route('/')
def index():
    result = repository.find_all()
    return render_template('payment/index.html', result=result)


@app.route('/detail/<payment_id>')
def detail(payment_id):
    payment = repository.find_by_id(payment_id)
    return render_template('payment/detail.html', payment=payment)
