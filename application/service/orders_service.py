from application.domain.orders_repository import OrdersRepository


class OrdersService:
    repository = OrdersRepository()

    def find_all(self, page, per_page):
        return self.repository.find_all(page, per_page)

    def find_by_id(self, orders_id):
        return self.repository.find_by_id(orders_id)
