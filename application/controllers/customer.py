from flask import Blueprint
from flask import abort
from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from application.controllers.form.customer_form import CustomerForm, PhotoForm
from application.domain.customer import Customer
from application.service.customer_service import CustomerService
from application.service.google import storage

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
    photo = PhotoForm()

    if form.validate_on_submit():
        customer.customer_number = form.customer_number.data
        customer.customer_name = form.customer_name.data
        customer.contact_last_name = form.contact_last_name.data
        customer.contact_first_name = form.contact_first_name.data
        customer.phone = form.phone.data or None
        customer.address_line1 = form.address_line1.data or None
        customer.address_line2 = form.address_line2.data or None
        customer.city = form.city.data or None
        customer.state = form.state.data or None
        customer.postal_code = form.postal_code.data or None
        customer.country = form.country.data or None
        customer.sales_rep_employee_number = form.sales_rep_employee_number.data or None
        customer.credit_limit = form.credit_limit.data or None
        file = photo.upload.data or None
        public_url = storage.upload_file(
            file.read(),
            file.filename,
            file.content_type
        )
        current_app.logger.debug(
            "Uploaded file %s as %s.", file.filename, public_url)

        service.save(customer)
        return redirect(url_for('.detail', customer_id=customer.id))
    current_app.logger.debug(form.errors)
    return render_template('customer/detail.html', form=form, photo=photo)


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
