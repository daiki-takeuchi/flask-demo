from flask import Blueprint
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
def detail(customer_id):
    customer = service.find_by_id(customer_id)
    form = CustomerForm(request.form)
    if request.method == 'POST' and form.validate():
        customer = Customer(request.form['customer_number'],
                            request.form['customer_name'],
                            request.form['contact_last_name'],
                            request.form['contact_first_name'],
                            request.form['phone'],
                            request.form['address_line1'],
                            request.form['address_line2'],
                            request.form['city'],
                            request.form['state'],
                            request.form['postal_code'],
                            request.form['country'],
                            request.form['sales_rep_employee_number'],
                            request.form['credit_limit'])
        service.save(customer)
        current_app.logger.debug(form.errors)
        return redirect(url_for('.detail', customer_id=customer.id))
    return render_template('customer/detail.html', customer=customer, form=form)
