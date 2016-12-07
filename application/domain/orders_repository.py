from application import db
from application.domain.orders import Orders


class OrdersRepository(object):

    def find_all(self, page, per_page):
        pagination = Orders.query.paginate(page, per_page)
        return pagination.items

    def find_by_id(self, orders_id):
        return Orders.query.filter(Orders.id == orders_id).one()

    def save(self, orders):
        db.session.add(orders)
        db.session.commit()
