from src.categories import Category
from src.products import LawnGrass, Smartphone

if __name__ == "__main__":
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
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
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
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны")
    category_grass = Category("Газонная трава", "Различные виды газонной травы")

    category_smartphones.add_product(smartphone1)
    category_smartphones.add_product(smartphone2)

    # category_grass.add_product(grass1)
    # category_grass.add_product(grass2)

    print(Category.avg_price(category_smartphones))

    # try:
    #     product_invalid = Smartphone(
    #         "Бракованный товар",
    #         "Неверное количество",
    #         1000.0,
    #         0,
    #         90.3,
    #         "Note 11",
    #         1024,
    #         "Синий",
    #     )
    #
    # except ValueError as e:
    #     print(
    #       "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
    #     )
    # else:
    #     print(
    #         "Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством"
    #     )
