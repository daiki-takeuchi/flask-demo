from flask import Blueprint
from flask import render_template

from application.domain.product_repository import ProductRepository

app = Blueprint('product', __name__)
repository = ProductRepository()

@app.route('/')
def index():
    result = repository.find_all()
    return render_template('product/index.html', result=result)


@app.route('/detail/<product_id>')
def detail(product_id):
    product = repository.find_by_id(product_id)
    return render_template('product/detail.html', product=product)
