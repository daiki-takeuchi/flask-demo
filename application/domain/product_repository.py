from flask import current_app

from application import db
from application.domain.product import Product


class ProductRepository(object):

    def find_all(self, page):
        pagination = Product.query.paginate(page, Product.PER_PAGE)
        return pagination

    def find_by_id(self, product_id):
        return Product.query.filter(Product.id == product_id).first()

    def save(self, product):
        db.session.add(product)
        db.session.commit()
        current_app.logger.debug('save:' + str(product))

    def destroy(self, product):
        db.session.delete(product)
        db.session.commit()
        current_app.logger.debug('destroy:' + str(product))
