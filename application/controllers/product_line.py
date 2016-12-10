from flask import Blueprint
from flask import render_template

from application.service.product_line_service import ProductLineService

bp = Blueprint('product_line', __name__, url_prefix='/productline')
service = ProductLineService()


@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/index/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    pagination = service.find_all(page)
    return render_template('product_line/index.html', pagination=pagination)


@bp.route('/page/<int:page>', methods=['GET', 'POST'])
def product_line_page(page=1):
    return index(page)


@bp.route('/detail/<product_line_id>')
def detail(product_line_id):
    product_line = service.find_by_id(product_line_id)
    return render_template('product_line/detail.html', product_line=product_line)
