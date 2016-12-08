from application.domain.product_line_repository import ProductLineRepository


class ProductLineService(object):
    repository = ProductLineRepository()

    def find_all(self, page):
        return self.repository.find_all(page)

    def find_by_id(self, product_line_id):
        return self.repository.find_by_id(product_line_id)
