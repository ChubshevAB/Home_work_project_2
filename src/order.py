from src.base_product_container import BaseProductContainer
from src.products import Product
from src.my_exception import ZeroQuantityError


class Order(BaseProductContainer):
    def __init__(self, product: "Product", quantity):
        try:
            if quantity <= 0:
                raise ZeroQuantityError("Невозможно создать заказ на товар с нулевым количеством.")

            super().__init__(product.name, product.description)
            self.product = product
            self.quantity = quantity
            self.total_cost = self.calculate_total_cost()

        except ZeroQuantityError as e:
            print(e)
        finally:
            print("Обработка создания заказа завершена.")

    def calculate_total_cost(self):
        return self.product.price * self.quantity

    def get_total_quantity(self):
        return self.quantity

    def products_info(self):
        return str(self.product)

    def __str__(self):
        return f"Заказ: {self.product.name}, количество: {self.quantity}, общая стоимость: {self.total_cost:.2f} руб."
