from application import db
from application.domain.payment import Payment


class PaymentRepository(object):

    def find_all(self, page):
        pagination = Payment.query.paginate(page, Payment.PER_PAGE)
        return pagination.items

    def find_by_id(self, payment_id):
        return Payment.query.filter(Payment.id ==  payment_id).one()

    def save(self, payment):
        db.session.add(payment)
        db.session.commit()
