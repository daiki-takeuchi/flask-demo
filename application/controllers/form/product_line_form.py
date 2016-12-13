from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, IntegerField, DecimalField, DateField


class ProductLineForm(FlaskForm):
    id = IntegerField('Id')
    product_line = StringField('Product Line', [validators.Length(max=32)])
    text_description = StringField('Text Description', [validators.Length(max=1024)])
    html_description = StringField('Html Description', [validators.Length(max=1024)])
    image = StringField('Image', [validators.Length(max=1024)])
    submit = SubmitField("Send")
