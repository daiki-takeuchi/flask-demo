from application import db
from application.domain.order_detail import OrderDetail


class OrderDetailRepository(object):

    def find_all(self, page, per_page):
        pagination = OrderDetail.query.paginate(page, per_page)
        return pagination

    def find_by_id(self, order_detail_id):
        return OrderDetail.query.filter(OrderDetail.id == order_detail_id).one()

    def save(self, order_detail):
        db.session.add(order_detail)
        db.session.commit()
