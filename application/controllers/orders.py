from flask import Blueprint
from flask import render_template

app = Blueprint('orders', __name__)


@app.route('/')
def index():
    result = []
    return render_template('orders/index.html', result=result)


@app.route('/detail/<id>')
def detail(id):
    orders = []
    return render_template('orders/detail.html', result=orders)
