from application.database import db_session
from application.domain.order_detail import OrderDetail


class OrderDetailRepository(object):

    def find_all(self):
        return db_session.query(OrderDetail).all()

    def find_by_id(self, order_detail_id):
        return db_session.query(OrderDetail).filter('order_detail.id = ' + order_detail_id).one()

    def save(self, order_detail):
        db_session.add(order_detail)
        db_session.commit()
