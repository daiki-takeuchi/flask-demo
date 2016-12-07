from application import db
from application.domain.product import Product


class ProductRepository(object):

    def find_all(self):
        return Product.query.all()

    def find_by_id(self, product_id):
        return Product.query.filter(Product.id ==  product_id).one()

    def save(self, product):
        db.session.add(product)
        db.session.commit()
