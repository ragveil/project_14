from typing import Any

import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


@pytest.fixture(scope="session")
def prod_1() -> Product:
    return Product("Nokia", "Connecting people", 7777.7, 13)


@pytest.fixture(scope="session")
def prod_2() -> Product:
    return Product("Mac", "Some people's dream", 999999.99, 8)


@pytest.fixture(scope="session")
def dict_prod() -> dict:
    return {"name": "TECNO SPARK 20 Pro+", "description": "256gb", "price": 16000.0, "quantity": 21}


@pytest.fixture(scope="session")
def dict_prod_1() -> dict:
    return {"name": "Nokia", "description": "Connecting people", "price": 6000.0, "quantity": 21}


@pytest.fixture(scope="session")
def some_category() -> Category:
    Category.category_count = 0
    Category.product_count = 0
    prod_1 = Product("Nokia", "Connecting people", 7777.7, 13)
    prod_2 = Product("Mac", "Some people's dream", 999999.99, 8)
    name = "Техника"
    descr = "Побочный продукт человеческой эволюции для удовлетворения его потребности в лени"
    products = [prod_1, prod_2]
    return Category(name, descr, products)


@pytest.fixture(scope="session")
def list_of_products() -> list:
    return [
        "Nokia, 7777.7 руб., Остаток: 13 шт.",
        "Mac, 999999.99 руб., Остаток: 8 шт.",
        "TECNO SPARK 20 Pro+, 16000.0 руб., Остаток: 21 шт.",
    ]


@pytest.fixture(scope="session")
def smartphone_1() -> Smartphone:
    return Smartphone("Infinix SMART 9", "64GB, Черный цвет, 13+0,08MP камера", 3999, 16, 46, "SMART 9", 64, "Черный")


@pytest.fixture(scope="session")
def smartphone_2() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy A16 4G", "256GB, Зеленый цвет, 50+5+2MP камера", 15999, 8, 51, "Galaxy A16 4G", 256, "Зеленый"
    )


@pytest.fixture(scope="session")
def smartphone_3() -> Smartphone:
    return Smartphone(
        "Apple iPhone 16 Pro",
        "256GB, Бежевый цвет, 48+48+12MP камера",
        121599,
        16,
        63,
        "iPhone 16 Pro",
        256,
        "Бежевый",
    )


@pytest.fixture(scope="session")
def lawn_grass_1() -> LawnGrass:
    return LawnGrass(
        "Быстрый газон",
        "Высокая приживаемость и быстрая скорость роста",
        709.5,
        12,
        "Беларусь",
        "6 дней",
        "Темно-зеленый",
    )


@pytest.fixture(scope="session")
def lawn_grass_2() -> LawnGrass:
    return LawnGrass(
        "Газон Сибиряк",
        "Морозоустойчивый газон, выдерживает температуры до -50С.",
        1649,
        7,
        "Россия",
        "12 дней",
        "Зеленый",
    )


@pytest.fixture(scope="session")
def other_class() -> Any:
    class Other:
        def __init__(self, name: str, price: float) -> None:
            self.name = name
            self.price = price

    return Other("Атака мурлоков", 18.18)


@pytest.fixture(scope="session")
def null_quantity() -> dict:
    return {"name": "Пустой товар", "description": "Пусто", "price": 99999, "quantity": 0}
