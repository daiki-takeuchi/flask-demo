from sqlalchemy import Column, Integer, String, Numeric

from application import db


class OrderDetail(db.Model):
    __tablename__ = 'order_detail'
    PER_PAGE = 10

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_number = Column(Integer, nullable=False)
    product_code = Column(String(32), nullable=False)
    quantity_ordered = Column(Integer, nullable=False)
    price_each = Column(Numeric(10,2))
    order_line_number = Column(Integer)

    def __init__(self,
                 order_number=None,
                 product_code=None,
                 quantity_ordered=None,
                 price_each=None,
                 order_line_number=None):
        self.order_number = order_number
        self.product_code = product_code
        self.quantity_ordered = quantity_ordered
        self.price_each = price_each or None
        self.order_line_number = order_line_number or None

    def __repr__(self):
        return "<OrderDetail:" + \
                "'id='{}".format(self.id) + \
                "', order_number='{}".format(self.order_number) + \
                "', product_code='{}".format(self.product_code) + \
                "', quantity_ordered='{}".format(self.quantity_ordered) + \
                "', price_each='{}".format(self.price_each) + \
                "', order_line_number='{}".format(self.order_line_number) + \
                "'>"
