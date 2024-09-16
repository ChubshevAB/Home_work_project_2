# class Product:
#     name: str
#     description: str
#     __price: float
#     quantity: int
#
#     def __init__(self, name, description, price, quantity):
#         self.name = name
#         self.description = description
#         self.__price = price
#         self.quantity = quantity
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         if value <= 0:
#             print("Цена не должна быть нулевая или отрицательная")
#         elif value < self.__price:
#             confirmation = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {value}? (y/n): ")
#             if confirmation.lower() == 'y':
#                 self.__price = value
#                 print(f"Цена успешно изменена на {value}.")
#             else:
#                 print("Изменение цены отменено.")
#         else:
#             self.__price = value
#
#     @classmethod
#     def new_product(cls, product_info: dict):
#         return cls(
#             name=product_info["name"],
#             description=product_info["description"],
#             price=product_info["price"],
#             quantity=product_info["quantity"],
#         )
#
#
# class Category:
#     name: str
#     description: str
#     __products: list
#     product_count = 0
#     category_count = 0
#
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#         self.__products = []
#         Category.category_count += 1
#
#
#     def add_product(self, product: Product):
#         for existing_product in self.__products:
#             if existing_product.name == product.name:
#                 existing_product.quantity += product.quantity
#                 existing_product.price = max(existing_product.price, product.price)
#                 return
#             else:
#                 self.__products.append(product)
#                 Category.product_count += len(Category.__products)
#
#
#     @property
#     def products(self):
#         products_str = ''
#         for product in self.__products:
#             products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
#         return products_str
