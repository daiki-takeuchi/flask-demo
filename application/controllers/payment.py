from flask import Blueprint
from flask import render_template

from application.domain.payment import Payment

app = Blueprint('payment', __name__)


@app.route('/')
def index():
    result = Payment.query.all()
    return render_template('payment/index.html', result=result)


@app.route('/detail/<payment_id>')
def detail(payment_id):
    payment = Payment.query.filter('payment.id = ' + payment_id).one()
    return render_template('payment/detail.html', payment=payment)
