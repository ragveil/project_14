from collections.abc import Iterable
from typing import Any

import pytest

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


def test_repr(prod_1: Product, some_category: Category) -> None:
    assert repr(prod_1) == "Nokia, Connecting people, 5555.5, 13"
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


def test_add(prod_1: Product, prod_2: Product) -> None:
    result = prod_1 + prod_2
    assert result == 8072221.42
