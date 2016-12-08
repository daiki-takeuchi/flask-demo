from application.domain.product_repository import ProductRepository


class ProductService:
    repository = ProductRepository()

    def find_all(self, page):
        return self.repository.find_all(page)

    def find_by_id(self, product_id):
        return self.repository.find_by_id(product_id)
