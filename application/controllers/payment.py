from flask import Blueprint
from flask import render_template

app = Blueprint('payment', __name__)

@app.route('/')
def payment_index():
    result = []
    return render_template('payment/index.html', result=result)

@app.route('/detail/<id>')
def payment_detail(id):
    payment = []
    return render_template('payment/detail.html', result=payment)
