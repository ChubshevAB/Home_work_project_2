import pytest

from src.categories import Category
from src.products import LawnGrass, Product, Smartphone


def test_product(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category(category):
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
        "функций для удобства жизни"
    )
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
    product_info = {
        "name": "Товар",
        "description": "Описание товара",
        "price": 100.0,
        "quantity": 10,
    }
    product = Product.new_product(product_info)
    assert product.name == "Товар"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    category = Category("Категория", "Описание категории")
    assert category.name == "Категория"
    assert category.description == "Описание категории"


def test_add_product():
    category = Category("Категория", "Описание категории")
    product_info = {
        "name": "Товар",
        "description": "Описание товара",
        "price": 100.0,
        "quantity": 10,
    }
    product = Product.new_product(product_info)
    category.add_product(product)
    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert product.name == "Товар"


def test_total_price():

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )

    assert smartphone1 + smartphone2 == 2580000.0


def test_total_price_error():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    try:
        result = smartphone1 + grass1
        assert result
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")


def test_zero_quantity():
    with pytest.raises(ValueError) as e:

        smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            0,
            95.5,
            "S23 Ultra",
            256,
            "Серый",
        )

    assert str(e.value) == "Товар с нулевым количеством не может быть добавлен"


def test_avg_price(capsys):

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны")
    result = Category.avg_price(category_smartphones)

    assert result == 0
