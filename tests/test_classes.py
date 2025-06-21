from src.classes import Category, Product


def test_product(prod_1: Product) -> None:
    assert prod_1.name == "Nokia"
    assert prod_1.description == "Connecting people"
    assert prod_1.price == 7777.7
    assert prod_1.quantity == 13


def test_category(some_category: Category) -> None:
    assert some_category.name == "Техника"
    assert (
        some_category.description == "Побочный продукт человеческой эволюции для удовлетворения его потребности в лени"
    )
    assert some_category.category_count == 1
    assert some_category.product_count == 2
    assert some_category.total_count == 21
