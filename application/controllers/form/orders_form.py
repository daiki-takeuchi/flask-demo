from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, IntegerField, DecimalField, DateField


class OrdersForm(FlaskForm):
    id = IntegerField('Id')
    order_number = IntegerField('Order Number', [validators.required()])
    order_date = DateField('Order Date', [validators.required()], format='%Y/%m/%d')
    required_date = DateField('Required Date', [validators.required()], format='%Y/%m/%d')
    shipped_date = DateField('Sipped Date', [validators.optional()], format='%Y/%m/%d')
    status = StringField('Status', [validators.Length(max=32)])
    comments = StringField('Comments', [validators.Length(max=256)])
    customer_number = IntegerField('Customer Number', [validators.optional()])
    submit = SubmitField("Send")
