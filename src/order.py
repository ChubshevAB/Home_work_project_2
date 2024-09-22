from src.base_product_container import BaseProductContainer
from src.products import Product


class Order(BaseProductContainer):
    def __init__(self, product: "Product", quantity):
        super().__init__(product.name, product.description)
        self.product = product
        self.quantity = quantity
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        return self.product.price * self.quantity

    def get_total_quantity(self):
        return self.quantity

    def products_info(self):
        return str(self.product)

    def __str__(self):
        return f"Заказ: {self.product.name}, количество: {self.quantity}, общая стоимость: {self.total_cost:.2f} руб."
