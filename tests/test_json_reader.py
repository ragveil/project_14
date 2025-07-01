from src.classes import Category, Product
from src.constants import PATH_TO_TEST_JSON
from src.json_reader import get_class_obj


def test_get_class_obj(prod_1: Product, prod_2: Product, some_category: Category) -> None:
    products, category = get_class_obj(PATH_TO_TEST_JSON)
    product1, product2 = products
    assert product1.name == prod_1.name
    assert product2.description == prod_2.description
