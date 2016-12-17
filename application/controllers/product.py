from flask import Blueprint
from flask import abort
from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from application.controllers.form.product_form import ProductForm
from application.domain.product import Product
from application.service.product_service import ProductService

bp = Blueprint('product', __name__, url_prefix='/product')
service = ProductService()


@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
def index(page=1):
    pagination = service.find_all(page)
    return render_template('product/index.html', pagination=pagination)


@bp.route('/page/<int:page>', methods=['GET', 'POST'])
def product_page(page=1):
    return index(page)


@bp.route('/detail/<product_id>', methods=['GET', 'POST'])
def detail(product_id=None):
    if product_id is not None:
        product = service.find_by_id(product_id)
    else:
        product = Product()
    current_app.logger.debug(str(product))

    if product is None and product_id is not None:
        return abort(404)
    form = ProductForm(request.form, product)

    if form.validate_on_submit():
        product.product_code = form.product_code.data
        product.product_name = form.product_name.data
        product.product_line = form.product_line.data
        product.product_scale = form.product_scale.data
        product.product_vendor = form.product_vendor.data
        product.product_description = form.product_description.data or None
        product.quantity_in_stock = form.quantity_in_stock.data or None
        product.buy_price = form.buy_price.data or None
        product.msrp = form.msrp.data or None

        service.save(product)
        return redirect(url_for('.detail', product_id=product.id))
    current_app.logger.debug(form.errors)
    return render_template('product/detail.html', form=form)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    return detail()


@bp.route('/delete/<product_id>', methods=['GET'])
def delete(product_id):
    product = service.find_by_id(product_id)
    if product is None:
        return redirect('/product')
    service.destroy(product)
    return redirect('/product')
