from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, IntegerField, DecimalField


class ProductForm(FlaskForm):
    id = IntegerField('Id')
    product_code = StringField('Product Code', [validators.required(), validators.Length(max=32)])
    product_name = StringField('Product Name', [validators.required(), validators.Length(max=128)])
    product_line = StringField('Product Line', [validators.required(), validators.Length(max=32)])
    product_scale = StringField('Product Scale', [validators.required(), validators.Length(max=32)])
    product_vendor = StringField('Product Vendor', [validators.required(), validators.Length(max=64)])
    product_description = StringField('Product Description', [validators.Length(max=1024)])
    quantity_in_stock = IntegerField('Quantity In Stock', [validators.optional()])
    buy_price = DecimalField('Buy Price', [validators.optional()])
    msrp = DecimalField('Msrp', [validators.optional()])
    submit = SubmitField("Send")
