#from src.classes_product_category import Product, Category
from src.products import Product
from src.categories import Category


def test_product(product):
    assert product.name == 'Samsung Galaxy S23 Ultra'
    assert product.description == '256GB, Серый цвет, 200MP камера'
    assert product.price == 180000.0
    assert product.quantity == 5

def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category.product_count == 0
    assert category.category_count == 1


def test_product_initialization():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product.price == 100.0
    assert product.quantity == 10


def test_price_setter_with_invalid_value():
    product = Product("Товар", "Описание товара", 100.0, 10)
    product.price = -50
    assert product.price == 100.0


def test_new_product_class_method():
    product_info = {"name": "Товар", "description": "Описание товара", "price": 100.0, "quantity": 10}
    product = Product.new_product(product_info)
    assert product.name == "Товар"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    category = Category("Категория", "Описание категории")
    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert category.products == ""


def test_add_product():
    category = Category("Категория", "Описание категории")
    product_info = {"name": "Товар", "description": "Описание товара", "price": 100.0, "quantity": 10}
    product = Product.new_product(product_info)
    category.add_product(product)
    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert product.name == "Товар"


