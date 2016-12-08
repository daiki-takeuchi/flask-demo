from application import db
from application.domain.product_line import ProductLine


class ProductLineRepository(object):

    def find_all(self, page):
        pagination = ProductLine.query.paginate(page, ProductLine.PER_PAGE)
        return pagination.items

    def find_by_id(self, product_line_id):
        return ProductLine.query.filter(ProductLine.id == product_line_id).one()

    def save(self, product_line):
        db.session.add(product_line)
        db.session.commit()
