from sqlalchemy import Column, Integer, String, Date

from application.config.database import Model


class Orders(Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_number = Column(Integer, nullable=False)
    order_date = Column(Date, nullable=False)
    required_date = Column(Date, nullable=False)
    shipped_date = Column(Date)
    status = Column(String(32))
    comments = Column(String(256))
    customer_number = Column(Integer)

    def __init__(self,
                 order_number=None,
                 order_date=None,
                 required_data=None,
                 shipped_date=None,
                 status=None,
                 comments=None):
        self.order_number = order_number
        self.order_date = order_date
        self.required_data = required_data
        self.shipped_date = shipped_date
        self.status = status
        self.comments = comments

    def __repr__(self):
        return '<Orders {}[ID:{}>'.format(self.order_number, self.id)
