from application.domain.payment_repository import PaymentRepository


class PaymentService(object):
    repository = PaymentRepository()

    def find_all(self, page):
        return self.repository.find_all(page)

    def find_by_id(self, payment_id):
        return self.repository.find_by_id(payment_id)

    def save(self, payment):
        return self.repository.save(payment)

    def destroy(self, payment):
        return self.repository.destroy(payment)
