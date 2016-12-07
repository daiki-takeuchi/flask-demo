from sqlalchemy import Column, Integer, String, Numeric

from application import db


class Customer(db.Model):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_number = Column(Integer, nullable=False)
    customer_name = Column(String(124), nullable=False)
    contact_last_name = Column(String(124), nullable=False)
    contact_first_name = Column(String(124), nullable=False)
    phone = Column(String(32))
    address_line1 = Column(String(124))
    address_line2 = Column(String(124))
    city = Column(String(32))
    state = Column(String(32))
    postal_code = Column(String(32))
    country = Column(String(32))
    sales_rep_employee_number = Column(Integer)
    credit_limit = Column(Numeric(10, 2))

    def __init__(self,
                 customer_number=None,
                 customer_name=None,
                 contact_last_name=None,
                 contact_first_name=None,
                 phone=None,
                 address_line1=None,
                 address_line2=None,
                 city=None,
                 state=None,
                 postal_code=None,
                 country=None,
                 sales_rep_employee_number=None,
                 credit_limit=None):
        self.customer_number = customer_number
        self.customer_name = customer_name
        self.contact_last_name = contact_last_name
        self.contact_first_name = contact_first_name
        self.phone = phone
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.sales_rep_employee_number = sales_rep_employee_number
        self.credit_limit = credit_limit

    def __repr__(self):
        return '<Customer {}[ID:{}>'.format(self.customer_name, self.id)
