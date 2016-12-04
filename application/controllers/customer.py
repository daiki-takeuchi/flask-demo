from flask import Blueprint
from flask import render_template

app = Blueprint('customer', __name__)

@app.route('/')
def customer_index():
    result = []
    return render_template('customer/index.html', result=result)

@app.route('/detail/<id>')
def customer_detail(id):
    customer = []
    return render_template('customer/detail.html', result=customer)
