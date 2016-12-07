from application import db
from application.domain.payment import Payment


class PaymentRepository(object):

    def find_all(self):
        return Payment.query.all()

    def find_by_id(self, payment_id):
        return Payment.query.filter(Payment.id ==  payment_id).one()

    def save(self, payment):
        db.session.add(payment)
        db.session.commit()
