from src.products import Product

class Category:
    name: str
    description: str
    __products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1


    def add_product(self, product: Product):
        for existing_product in self.__products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                existing_product.price = max(existing_product.price, product.price)
                return
            else:
                self.__products.append(product)
                Category.product_count += len(Category.__products)


    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
