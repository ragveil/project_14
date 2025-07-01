from typing import Any


class Product:
    """
    Класс для представления продукта.
    """

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Метод для инициализации экземпляра класса продукта.
        :param name: Наименование продукта, str.
        :param description: Описание продукта, str.
        :param price: Цена продукта, float.
        :param quantity: Количество продуктов, int.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"

    @classmethod
    def new_product(cls, prod_dict: dict, products: "Category") -> Any:
        if prod_dict.keys() == {"name", "description", "price", "quantity"}:
            name, description, price, quantity = prod_dict.values()
            for item in products.products:
                if item.name == name:
                    quantity += item.quantity
                    price = max(price, item.price)
                else:
                    return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> Any:
        if new_price <= 0:
            print(f'Неверно задано значение цены - "{new_price}".')
        elif new_price < self.price:
            answer = input(
                f'Цена {new_price} ниже установленной {self.__price}. Введите "Y", чтобы выбрать {new_price} цену.'
            )
            if answer.lower() == "y":
                self.__price = new_price
            else:
                print(f"Цена осталась без изменений - {self.__price}.")


class Category:
    """
    Класс для представления категории.
    """

    product_count: int = 0
    category_count: int = 0
    product_list: list[Product]

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Метод для инициализации экземпляра класса категории.
        :param name: Наименование категории, str.
        :param description: Описание категории, str.
        :param products: Список продуктов, list[Product].
        """
        self.name = name
        self.description = description
        self.__products = products
        self.total_count = sum(product.quantity for product in products)
        Category.category_count += 1

    def add_product(self, product: Product) -> Any:
        """
        Добавляет продукт в категорию.
        :param product:
        :return:
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count = len(self.__products)

    @property
    def products(self) -> list[Product]:
        """
        Выводит список продуктов.
        :return:
        """
        return self.__products

    @property
    def products_list(self) -> list:
        list_of_products = []
        for product in self.__products:
            list_of_products.append(f"{product.name}, {product.price} руб., Остаток: {product.quantity} шт.")
        return list_of_products
