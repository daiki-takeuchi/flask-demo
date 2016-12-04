from sqlalchemy import Column, Integer, String, Numeric

from application.config.database import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_code = Column(String(32), nullable=False)
    product_name = Column(String(128), nullable=False)
    product_line = Column(String(32), nullable=False)
    product_scale = Column(String(32), nullable=False)
    product_vendor = Column(String(64), nullable=False)
    product_description = Column(String(1024))
    quantity_in_stock = Column(Integer)
    buy_price = Column(Numeric(10, 2))
    msrp = Column(Numeric(10, 2))

    def __init__(self,
                 product_code=None,
                 product_name=None,
                 product_line=None,
                 product_scale=None,
                 product_vendor=None,
                 product_description=None,
                 quantity_in_stock=None,
                 buy_price=None,
                 msrp=None):
        self.product_code = product_code
        self.product_name = product_name
        self.product_line = product_line
        self.product_scale = product_scale
        self.product_vendor = product_vendor
        self.product_description = product_description
        self.quantity_in_stock = quantity_in_stock
        self.buy_price = buy_price
        self.msrp = msrp

    def __repr__(self):
        return '<Customer {}[ID:{}>'.format(self.customer_name, self.id)
