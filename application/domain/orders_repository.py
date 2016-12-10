from application import db
from application.domain.orders import Orders


class OrdersRepository(object):

    def find_all(self, page):
        pagination = Orders.query.paginate(page, Orders.PER_PAGE)
        return pagination

    def find_by_id(self, orders_id):
        return Orders.query.filter(Orders.id == orders_id).one()

    def save(self, orders):
        db.session.add(orders)
        db.session.commit()
