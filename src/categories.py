from src.base_product_container import BaseProductContainer
from src.products import Product
from src.my_exception import ZeroQuantityError


class Category(BaseProductContainer):
    name: str
    description: str
    _products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description):
        super().__init__(name, description)
        # self.name = name
        # self.description = description
        self._products = []
        Category.category_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        return self._products

    def add_product(self, product: Product):
        try:
            if product.quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен.")

            if not isinstance(product, Product):
                raise TypeError

            for existing_product in self._products:
                if existing_product.name == product.name:
                    existing_product.quantity += product.quantity
                    existing_product.price = max(existing_product.price, product.price)
                    return

            self._products.append(product)
            Category.product_count += 1
            print(f"Товар {product.name} успешно добавлен в категорию.")

        except ZeroQuantityError as e:
            print(e)
        finally:
            print("Обработка добавления товара завершена.")

    @property
    def products_info(self):
        products_str = ""
        for product in self._products:
            products_str += f"{str(product)}\n"
        return products_str

    def avg_price(self):

        try:
            total_price = sum(product.price for product in self._products)
            avg_price = total_price / Category.product_count
            return avg_price

        except ZeroDivisionError:
            print("В категории нет товаров")
            return 0
