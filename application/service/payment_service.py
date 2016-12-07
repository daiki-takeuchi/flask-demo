from application.domain.payment_repository import PaymentRepository


class PaymentService:
    repository = PaymentRepository()

    def find_all(self, page, per_page):
        return self.repository.find_all(page, per_page)

    def find_by_id(self, payment_id):
        return self.repository.find_by_id(payment_id)
