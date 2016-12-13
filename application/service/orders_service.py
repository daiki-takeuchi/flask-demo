from application.domain.orders_repository import OrdersRepository


class OrdersService(object):
    repository = OrdersRepository()

    def find_all(self, page):
        return self.repository.find_all(page)

    def find_by_id(self, orders_id):
        return self.repository.find_by_id(orders_id)

    def save(self, orders):
        return self.repository.save(orders)

    def destroy(self, orders):
        return self.repository.destroy(orders)
