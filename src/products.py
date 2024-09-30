from src.base_product import BaseProduct, MixinProd


class Product(BaseProduct, MixinProd):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if self.quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток {self.quantity} шт."

    def __add__(self, other):
        if isinstance(self, Smartphone) and isinstance(other, Smartphone):
            total_price = self.__price * self.quantity + other.__price * other.quantity
            return total_price
        elif isinstance(self, LawnGrass) and isinstance(other, LawnGrass):
            total_price = self.__price * self.quantity + other.__price * other.quantity
            return total_price
        else:
            raise TypeError

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


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
