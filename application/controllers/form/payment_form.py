from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, IntegerField, DecimalField, DateField


class PaymentForm(FlaskForm):
    id = IntegerField('Id')
    customer_number = IntegerField('Customer Number', [validators.required()])
    check_number = StringField('Check Number', [validators.Length(max=64)])
    payment_date = DateField('Required Date', [validators.required()], format='%Y/%m/%d')
    amount = DecimalField('Amount', [validators.optional()])
    submit = SubmitField("Send")
