from flask import Blueprint
from flask import render_template

from application.domain.product_line import ProductLine

app = Blueprint('product_line', __name__)


@app.route('/')
def index():
    result = ProductLine.query.all()
    return render_template('product_line/index.html', result=result)


@app.route('/detail/<product_line_id>')
def detail(product_line_id):
    product_line = ProductLine.query.filter('product_line.id = ' + product_line_id).one()
    return render_template('product_line/detail.html', product_line=product_line)
