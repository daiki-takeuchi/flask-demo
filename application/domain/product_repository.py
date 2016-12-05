from application.config.database import db_session
from application.domain.product import Product


class ProductRepository(object):

    def find_all(self):
        return db_session.query(Product).all()

    def find_by_id(self, product_id):
        return db_session.query(Product).filter('product.id = ' + product_id).one()

    def save(self, product):
        db_session.add(product)
        db_session.commit()
