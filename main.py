# from src.classes_product_category import Product, Category
from src.categories import Category
from src.products import Product

if __name__ == "__main__":
    product1 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    product2 = Product.new_product(
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8,
        }
    )
    product3 = Product.new_product(
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14,
        }
    )

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )

    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)
    print(category1.products_info)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy Note 8",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 150000.0,
            "quantity": 7,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
