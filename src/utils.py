import json
import os

from src.classes_product_category import Product, Category

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Data', 'products.json'))


def read_json(path: str) -> list:
    with open(file_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    categories = []
    for category in data:
        products = []
        for prod in category['products']:
            products.append(Product(**prod))
        category['products'] = products
        categories.append(Category(**category))

    return categories

if __name__ == '__main__':
    data = read_json(file_path)
    product_data = create_objects_from_json(data)
    print(data)
    print(product_data)
