from application.domain.customer_repository import CustomerRepository


class CustomerService:
    repository = CustomerRepository()

    def find_all(self, page, per_page):
        return self.repository.find_all(page, per_page)

    def find_by_id(self, customer_id):
        return self.repository.find_by_id(customer_id)
