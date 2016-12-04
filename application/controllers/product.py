from flask import Blueprint
from flask import render_template

app = Blueprint('product', __name__)


@app.route('/')
def index():
    result = []
    return render_template('product/index.html', result=result)


@app.route('/detail/<id>')
def detail(id):
    product = []
    return render_template('product/detail.html', result=product)
