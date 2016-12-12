from flask import current_app

from application import db
from application.domain.customer import Customer


class CustomerRepository(object):

    def find_all(self, page):
        pagination = Customer.query.paginate(page, Customer.PER_PAGE)
        return pagination

    def find_by_id(self, customer_id):
        return Customer.query.filter(Customer.id == customer_id).first()

    def save(self, customer):
        db.session.add(customer)
        db.session.commit()
        current_app.logger.debug('save:' + str(customer))

    def destroy(self, customer):
        db.session.delete(customer)
        db.session.commit()
        current_app.logger.debug('destroy:' + str(customer))
