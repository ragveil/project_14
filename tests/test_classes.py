from collections.abc import Iterable
from typing import Any, Type

import pytest

from src.classes import Category, LawnGrass, MyException, Order, Product, Smartphone


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


def test_new_product_new(dict_prod: dict, some_category: Category) -> None:
    new_product = Product.new_product(dict_prod, some_category)
    assert new_product.name == dict_prod["name"]
    assert new_product.description == dict_prod["description"]
    assert new_product.price == dict_prod["price"]
    assert new_product.quantity == dict_prod["quantity"]


def test_new_product_update(dict_prod_1: dict, some_category: Category) -> None:
    new_product = Product.new_product(dict_prod_1, some_category)
    assert new_product.name == dict_prod_1["name"]
    assert new_product.quantity == dict_prod_1["quantity"] + some_category.products[0].quantity
    assert new_product.price == max(dict_prod_1["price"], new_product.price)


def test_price(prod_1: Product) -> None:
    assert prod_1.price == 7777.7


def test_price_say_yes(prod_1: Product, monkeypatch: Any) -> None:
    price_1 = 5555.5
    monkeypatch.setattr("builtins.input", lambda _: "y")
    prod_1.price = price_1
    assert prod_1.price == price_1


def test_price_say_no(prod_2: Product, monkeypatch: Any) -> None:
    price_2 = 1111.1
    monkeypatch.setattr("builtins.input", lambda _: "n")
    prod_2.price = price_2
    assert prod_2.price == 999999.99


@pytest.mark.parametrize("price, expected", [(0.0, 5555.5), (-5000.0, 5555.5)])
def test_price_incorrect(prod_1: Product, price: float, expected: float) -> None:
    prod_1.price = price
    assert prod_1.price == expected


def test_add_product(dict_prod: dict, some_category: Category) -> None:
    product = Product.new_product(dict_prod, some_category)
    some_category.add_product(product)
    assert some_category.product_count == 3
    assert some_category.category_count == 1
    assert some_category.products[2].name == product.name


def test_add_product_incorrect(some_category: Category, other_class: Any) -> None:
    with pytest.raises(TypeError):
        some_category.add_product(other_class)


def test_repr(prod_1: Product, some_category: Category) -> None:
    assert repr(prod_1) == "Product: ('Nokia', 'Connecting people', 5555.5, 13)"
    assert (
        repr(some_category)
        == "Техника, Побочный продукт человеческой эволюции для удовлетворения его потребности в лени, 42, 3"
    )


def test_str(prod_1: Product, some_category: Category) -> None:
    assert str(prod_1) == "Nokia, 5555.5 руб., Остаток: 13 шт."
    assert str(some_category) == "Техника, количество продуктов: 42 шт."


def test_iteration(some_category: Category) -> None:
    some_iter = isinstance(some_category, Iterable)
    assert some_iter is True


def test_add_prod(prod_1: Product, prod_2: Product) -> None:
    result = prod_1 + prod_2
    assert result == 8072221.42


def test_add_lawn(lawn_grass_1: LawnGrass, lawn_grass_2: LawnGrass) -> None:
    result = lawn_grass_1 + lawn_grass_2
    assert result == 20057.0


def test_add_smartphone(smartphone_1: Smartphone, smartphone_2: Smartphone) -> None:
    result = smartphone_1 + smartphone_2
    assert result == 191976


def test_add_incorrect(smartphone_1: Smartphone, lawn_grass_2: LawnGrass) -> None:
    with pytest.raises(TypeError):
        smartphone_1 + lawn_grass_2


@pytest.mark.parametrize(
    "class_1, class_2, expected",
    [
        (Smartphone, Product, True),
        (LawnGrass, Product, True),
        (Smartphone, Category, False),
        (LawnGrass, Category, False),
        (Category, Product, False),
    ],
)
def test_sub(
    class_1: Type[Smartphone | LawnGrass | Product], class_2: Type[Product | Category], expected: bool
) -> None:
    assert issubclass(class_1, class_2) == expected


def test_smartphone(smartphone_1: Smartphone) -> None:
    assert smartphone_1.efficiency == 46
    assert smartphone_1.model == "SMART 9"
    assert smartphone_1.memory == 64
    assert smartphone_1.color == "Черный"


def test_lawn_grass(lawn_grass_1: LawnGrass) -> None:
    assert lawn_grass_1.color == "Темно-зеленый"
    assert lawn_grass_1.germination_period == "6 дней"
    assert lawn_grass_1.country == "Беларусь"


@pytest.mark.parametrize(
    "quantity, expected",
    [
        (3, "Ваш заказ Nokia, Connecting people, 3 шт. на сумму 16666.5 руб. сформирован."),
        (33, "На складе нет такого количества товаров."),
    ],
)
def test_order(prod_1: Product, quantity: int, expected: str) -> None:
    ordered = Order(prod_1, quantity)
    assert str(ordered) == expected


def test_exception_product(null_quantity: dict, some_category: Category) -> None:
    with pytest.raises(MyException):
        Product.new_product(null_quantity, some_category)


def test_exception_order(prod_1: Product) -> None:
    with pytest.raises(MyException):
        Order(prod_1, 0)


def test_mid_price(some_category: Category) -> None:
    assert some_category.middle_price() == 341259.23


def test_zero_division() -> None:
    assert Category("Пусто", "Пусто", []).middle_price() == 0
