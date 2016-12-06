from sqlalchemy import Column, Integer, String, Numeric

from application import Model


class OrderDetail(Model):
    __tablename__ = 'order_detail'
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
        self.price_each = price_each
        self.order_line_number = order_line_number

    def __repr__(self):
        return '<OrderDetail {}[ID:{}>'.format(self.order_number, self.id)
