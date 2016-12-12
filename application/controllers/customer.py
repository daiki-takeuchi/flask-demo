from flask import Blueprint
from flask import abort
from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from application.controllers.form.customer_form import CustomerForm
from application.domain.customer import Customer
from application.service.customer_service import CustomerService

bp = Blueprint('customer', __name__, url_prefix='/customer')
service = CustomerService()


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET', 'POST'])
def index(page=1):
    pagination = service.find_all(page)
    return render_template('customer/index.html', pagination=pagination)


@bp.route('/page/<int:page>', methods=['GET', 'POST'])
def customer_page(page=1):
    return index(page)


@bp.route('/detail/<customer_id>', methods=['GET', 'POST'])
def detail(customer_id=None):
    if customer_id is not None:
        customer = service.find_by_id(customer_id)
    else:
        customer = Customer()
    current_app.logger.debug(str(customer))

    if customer is None and customer_id is not None:
        return abort(404)
    form = CustomerForm(request.form, customer)

    if request.method == 'POST' and form.validate():
        customer.customer_number = request.form['customer_number']
        customer.customer_name = request.form['customer_name']
        customer.contact_last_name = request.form['contact_last_name']
        customer.contact_first_name = request.form['contact_first_name']
        customer.phone = request.form['phone'] or None
        customer.address_line1 = request.form['address_line1'] or None
        customer.address_line2 = request.form['address_line2'] or None
        customer.city = request.form['city'] or None
        customer.state = request.form['state'] or None
        customer.postal_code = request.form['postal_code'] or None
        customer.country = request.form['country'] or None
        customer.sales_rep_employee_number = request.form['sales_rep_employee_number'] or None
        customer.credit_limit = request.form['credit_limit'] or None

        service.save(customer)
        return redirect(url_for('.detail', customer_id=customer.id))
    current_app.logger.debug(form.errors)
    return render_template('customer/detail.html', form=form)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    return detail()


@bp.route('/delete/<customer_id>', methods=['GET'])
def delete(customer_id):
    customer = service.find_by_id(customer_id)
    if customer is None:
        return redirect('/customer')
    service.destroy(customer)
    return redirect('/customer')
