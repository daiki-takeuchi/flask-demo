from flask import Blueprint
from flask import render_template

from application.domain.product_line_repository import ProductLineRepository

app = Blueprint('product_line', __name__)
repository = ProductLineRepository()

@app.route('/')
def index():
    result = repository.find_all()
    return render_template('product_line/index.html', result=result)


@app.route('/detail/<product_line_id>')
def detail(product_line_id):
    product_line = repository.find_by_id(product_line_id)
    return render_template('product_line/detail.html', product_line=product_line)
