from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, IntegerField, DecimalField


class CustomerForm(FlaskForm):
    id = IntegerField('Id')
    customer_number = IntegerField('Customer Number', [validators.required()])
    customer_name = StringField('Customer Name', [validators.required(), validators.Length(max=124)])
    contact_last_name = StringField('Contact Last Name', [validators.required(), validators.Length(max=124)])
    contact_first_name = StringField('Contact First Name', [validators.required(), validators.Length(max=124)])
    phone = StringField('Phone', [validators.Length(max=32)])
    address_line1 = StringField('Address Line1', [validators.Length(max=124)])
    address_line2 = StringField('Address Line2', [validators.Length(max=124)])
    city = StringField('City', [validators.Length(max=32)])
    state = StringField('State', [validators.Length(max=32)])
    postal_code = StringField('Postal Code', [validators.Length(max=32)])
    country = StringField('Country', [validators.Length(max=32)])
    sales_rep_employee_number = IntegerField('Sales Rep Employee Number')
    credit_limit = DecimalField('Credit Limit')
    submit = SubmitField("Send")
