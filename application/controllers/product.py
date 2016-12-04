from flask import Blueprint
from flask import render_template

from application.domain.product import Product

app = Blueprint('product', __name__)


@app.route('/')
def index():
    result = Product.query.all()
    return render_template('product/index.html', result=result)


@app.route('/detail/<product_id>')
def detail(product_id):
    product = Product.query.filter('product.id = ' + product_id).one()
    return render_template('product/detail.html', product=product)
