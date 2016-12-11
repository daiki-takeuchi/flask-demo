from application.domain.customer_repository import CustomerRepository


class CustomerService(object):
    repository = CustomerRepository()

    def find_all(self, page):
        return self.repository.find_all(page)

    def find_by_id(self, customer_id):
        return self.repository.find_by_id(customer_id)

    def save(self, customer):
        return self.repository.save(customer)
