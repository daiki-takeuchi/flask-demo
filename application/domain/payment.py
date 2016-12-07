from sqlalchemy import Column, Integer, String, Date, Numeric

from application import db


class Payment(db.Model):
    __tablename__ = 'payment'
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
        self.amount = amount

    def __repr__(self):
        return '<Payment {}[ID:{}>'.format(self.customer_number, self.id)
