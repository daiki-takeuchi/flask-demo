from application.config.database import db_session
from application.domain.product_line import ProductLine


class ProductLineRepository(object):

    def find_all(self):
        return db_session.query(ProductLine).all()

    def find_by_id(self, product_line_id):
        return db_session.query(ProductLine).filter('product_line.id = ' + product_line_id).one()

    def save(self, product_line):
        db_session.add(product_line)
        db_session.commit()
