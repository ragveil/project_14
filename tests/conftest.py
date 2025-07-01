import pytest

from src.classes import Category, Product


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
