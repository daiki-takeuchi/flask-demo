from flask import Blueprint
from flask import render_template

app = Blueprint('product_line', __name__)


@app.route('/')
def index():
    result = []
    return render_template('product_line/index.html', result=result)


@app.route('/detail/<id>')
def detail(id):
    product_line = []
    return render_template('product_line/detail.html', result=product_line)
