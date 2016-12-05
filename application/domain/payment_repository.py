from application.config.database import db_session
from application.domain.payment import Payment


class PaymentRepository(object):

    def find_all(self):
        return db_session.query(Payment).all()

    def find_by_id(self, payment_id):
        return db_session.query(Payment).filter('payment.id = ' + payment_id).one()

    def save(self, payment):
        db_session.add(payment)
        db_session.commit()
