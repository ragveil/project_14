import pytest

from src.classes import Category, Product


@pytest.fixture(scope="session")
def prod_1() -> Product:
    return Product("Nokia", "Connecting people", 7777.7, 13)


@pytest.fixture(scope="session")
def prod_2() -> Product:
    return Product("Mac", "Some people's dream", 999999.99, 8)


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
