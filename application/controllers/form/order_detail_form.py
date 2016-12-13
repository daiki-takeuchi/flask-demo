from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, IntegerField, DecimalField


class OrderDetailForm(FlaskForm):
    id = IntegerField('Id')
    order_number = IntegerField('Order Number', [validators.required()])
    product_code = StringField('Product Code', [validators.required(), validators.Length(max=32)])
    quantity_ordered = IntegerField('Quantity Ordered', [validators.optional()])
    price_each = DecimalField('Price Each', [validators.optional()])
    order_line_number = IntegerField('Order Line Number', [validators.optional()])
    submit = SubmitField("Send")
