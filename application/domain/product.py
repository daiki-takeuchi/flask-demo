from sqlalchemy import Column, Integer, String, Numeric

from application import db


class Product(db.Model):
    __tablename__ = 'product'
    PER_PAGE = 10

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
        self.product_description = product_description or None
        self.quantity_in_stock = quantity_in_stock or None
        self.buy_price = buy_price or None
        self.msrp = msrp or None

    def __repr__(self):
        return "<Customer:" + \
                "'id='{}".format(self.id) + \
                "', product_code='{}".format(self.product_code) + \
                "', product_name='{}".format(self.product_name) + \
                "', product_line='{}".format(self.product_line) + \
                "', product_scale='{}".format(self.product_scale) + \
                "', product_vendor='{}".format(self.product_vendor) + \
                "', product_description='{}".format(self.product_description) + \
                "', quantity_in_stock='{}".format(self.quantity_in_stock) + \
                "', buy_price='{}".format(self.buy_price) + \
                "', msrp='{}".format(self.msrp) + \
                "'>"
