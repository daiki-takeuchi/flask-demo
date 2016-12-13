from flask import current_app

from application import db
from application.domain.orders import Orders


class OrdersRepository(object):

    def find_all(self, page):
        pagination = Orders.query.paginate(page, Orders.PER_PAGE)
        return pagination

    def find_by_id(self, orders_id):
        return Orders.query.filter(Orders.id == orders_id).first()

    def save(self, orders):
        db.session.add(orders)
        db.session.commit()
        current_app.logger.debug('save:' + str(orders))

    def destroy(self, orders):
        db.session.delete(orders)
        db.session.commit()
        current_app.logger.debug('destroy:' + str(orders))
