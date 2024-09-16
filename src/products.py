class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirmation = input(
                f"Вы уверены, что хотите понизить цену с {self.__price} до {value}? (y/n): "
            )
            if confirmation.lower() == "y":
                self.__price = value
                print(f"Цена успешно изменена на {value}.")
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_info: dict):
        return cls(
            name=product_info["name"],
            description=product_info["description"],
            price=product_info["price"],
            quantity=product_info["quantity"],
        )
