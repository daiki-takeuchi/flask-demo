from application.domain.product_line_repository import ProductLineRepository


class ProductLineService:
    repository = ProductLineRepository()

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, product_line_id):
        return self.repository.find_by_id(product_line_id)
