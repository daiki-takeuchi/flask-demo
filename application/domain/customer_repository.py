from application.database import db_session
from application.domain.customer import Customer


class CustomerRepository(object):

    def find_all(self):
        return db_session.query(Customer).all()

    def find_by_id(self, customer_id):
        return db_session.query(Customer).filter('customer.id = ' + customer_id).one()

    def save(self, customer):
        db_session.add(customer)
        db_session.commit()
