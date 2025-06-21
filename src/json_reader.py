import json

from src.classes import Category, Product
from src.constants import PATH_TO_JSON


def get_class_obj(path: str) -> tuple[list[Product], list]:
    """
    Функция для инициализаций продуктов и категорий из JSON-файла.
    :param path: Путь к файлу, str.
    :return: Результат работы функции, кортеж со списками продуктов и категорий.
    """
    with open(path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    prods = []
    cats = []
    for item in data:
        for product in item["products"]:
            prods.append(
                Product(
                    str(product["name"]),
                    str(product["description"]),
                    float(product["price"]),
                    int(product["quantity"]),
                )
            )
        cats.append(Category(item["name"], item["description"], prods))
    return prods, cats


products, categories = get_class_obj(PATH_TO_JSON)

if __name__ == "__main__":  # pragma: no cover
    # Проверка результата по продуктам
    product1, product2, product3, product4 = products
    print(product1.name)
    print(product2.description)
    print(product3.price)
    print(product4.quantity)
    # Проверка результата по категориям
    category1, category2 = categories
    print(category1.name)
    print(category2.description)
    print(category1.total_count)
    print(category2.total_count)
    print(Category.product_count)
    print(Category.category_count)
