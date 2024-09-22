from src.order import Order
from src.products import Smartphone


def test_order(capsys):
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
    order = Order(smartphone1, 2)

    assert order.product.name == "Samsung Galaxy S23 Ultra"
    assert order.description == "256GB, Серый цвет, 200MP камера"
    assert order.total_cost == smartphone1.price * order.quantity
