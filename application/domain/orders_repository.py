from application.config.database import db_session
from application.domain.orders import Orders


class OrdersRepository(object):

    def find_all(self):
        return db_session.query(Orders).all()

    def find_by_id(self, orders_id):
        return db_session.query(Orders).filter('orders.id = ' + orders_id).one()

    def save(self, orders):
        db_session.add(orders)
        db_session.commit()
