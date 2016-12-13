from flask import Blueprint
from flask import abort
from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from application.controllers.form.product_line_form import ProductLineForm
from application.domain.product_line import ProductLine
from application.service.product_line_service import ProductLineService

bp = Blueprint('product_line', __name__, url_prefix='/productline')
service = ProductLineService()


@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
def index(page=1):
    pagination = service.find_all(page)
    return render_template('product_line/index.html', pagination=pagination)


@bp.route('/page/<int:page>', methods=['GET', 'POST'])
def product_line_page(page=1):
    return index(page)


@bp.route('/detail/<product_line_id>', methods=['GET', 'POST'])
def detail(product_line_id=None):
    if product_line_id is not None:
        product_line = service.find_by_id(product_line_id)
    else:
        product_line = ProductLine()
    current_app.logger.debug(str(product_line))

    if product_line is None and product_line_id is not None:
        return abort(404)
    form = ProductLineForm(request.form, product_line)

    if request.method == 'POST' and form.validate():
        product_line.product_line = request.form['product_line']
        product_line.text_description = request.form['text_description'] or None
        product_line.html_description = request.form['html_description'] or None
        product_line.image = request.form['image'] or None

        service.save(product_line)
        return redirect(url_for('.detail', product_line_id=product_line.id))
    current_app.logger.debug(form.errors)
    return render_template('product_line/detail.html', form=form)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    return detail()


@bp.route('/delete/<product_line_id>', methods=['GET'])
def delete(product_line_id):
    orders = service.find_by_id(product_line_id)
    if orders is None:
        return redirect('/product_line')
    service.destroy(orders)
    return redirect('/product_line')
