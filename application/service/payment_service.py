from application.domain.payment_repository import PaymentRepository


class PaymentService:
    repository = PaymentRepository()

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, payment_id):
        return self.repository.find_by_id(payment_id)
