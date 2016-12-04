from flask import Blueprint
from flask import render_template

app = Blueprint('payment', __name__)


@app.route('/')
def index():
    result = []
    return render_template('payment/index.html', result=result)


@app.route('/detail/<id>')
def detail(id):
    payment = []
    return render_template('payment/detail.html', result=payment)
