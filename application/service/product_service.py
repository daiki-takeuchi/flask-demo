from application.domain.product_repository import ProductRepository


class ProductService:
    repository = ProductRepository()

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, product_id):
        return self.repository.find_by_id(product_id)
