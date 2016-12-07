from application import db
from application.domain.customer import Customer


class CustomerRepository(object):

    def find_all(self, page, per_page):
        pagination = Customer.query.paginate(page, per_page)
        return pagination.items

    def find_by_id(self, customer_id):
        return Customer.query.filter(Customer.id == customer_id).one()

    def save(self, customer):
        db.session.add(customer)
        db.session.commit()
