from flask import Blueprint
from flask import render_template

from application.service.product_service import ProductService

bp = Blueprint('product', __name__, url_prefix='/product')
service = ProductService()

@bp.route('/')
def index():
    result = service.find_all()
    return render_template('product/index.html', result=result)


@bp.route('/detail/<product_id>')
def detail(product_id):
    product = service.find_by_id(product_id)
    return render_template('product/detail.html', product=product)
