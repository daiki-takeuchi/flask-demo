from sqlalchemy import Column, Integer, String, Date, Numeric

from application import db


class Payment(db.Model):
    __tablename__ = 'payment'
    PER_PAGE = 10

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_number = Column(Integer, nullable=False)
    check_number = Column(String(64), nullable=False)
    payment_date = Column(Date, nullable=False)
    amount = Column(Numeric(10, 2))

    def __init__(self,
                 customer_number=None,
                 check_number=None,
                 payment_date=None,
                 amount=None):
        self.customer_number = customer_number
        self.check_number = check_number
        self.payment_date = payment_date
        self.amount = amount or None

    def __repr__(self):
        return "<Payment:" + \
                "'id='{}".format(self.id) + \
                "', customer_number='{}".format(self.customer_number) + \
                "', check_number='{}".format(self.check_number) + \
                "', payment_date='{}".format(self.payment_date) + \
                "', amount='{}".format(self.amount) + \
                "'>"
