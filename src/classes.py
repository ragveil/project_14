from typing import Any, Iterator


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
        """
        Метод для информативного отображения объектов класса.
        :return: Строковое представление продукта, str.
        """
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"

    def __str__(self) -> str:
        """
        Метод для строкового представления объектов класса.
        :return: Строковый вывод информации о продукте, str.
        """
        return f"{self.name}, {self.price} руб., Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Метод для сложения общей стоимости двух продуктов.
        :param other: Второй продукт для суммирования.
        :return: Общая стоимость всех продуктов, float.
        """
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, prod_dict: dict, products: "Category") -> Any:
        """
        Метод для добавления нового продукта.
        :param prod_dict: Словарь с данными о продукте, dict.
        :param products: Продукты, уже добавленные в категорию.
        :return:
        """
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
        """
        Метод для возвращения значения цены.
        :return: Цена, float.
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> Any:
        """
        Метод для установки новой цены.
        :param new_price: Новая цена, float.
        :return:
        """
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
    # total_count: int = 0
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
        Category.category_count += 1

    def __repr__(self) -> str:
        """
        Метод для информативного отображения объектов класса.
        :return: Строковое представление категории, str.
        """
        return f"{self.name}, {self.description}, {self.total_count}, {self.product_count}"

    def __str__(self) -> str:
        """
        Метод для строкового представления объектов класса.
        :return: Строковый вывод информации о категории, str.
        """
        return f"{self.name}, количество продуктов: {self.total_count} шт."

    def add_product(self, product: Product) -> Any:
        """
        Добавляет продукт в категорию.
        :param product: Продукт, добавляемый в категорию.
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
    def total_count(self) -> int:
        """
        Метод для подсчета общего количества единиц каждого продукта в категории.
        :return:
        """
        result = 0
        for product in self.__products:
            result += product.quantity
        return result

    def __iter__(self) -> Iterator[Product]:
        """
        Метод для получения итератора по объектам класса.
        :return:
        """
        return ProdIteration(self)


class ProdIteration:  # pragma: no cover
    """
    Класс для итерации по продуктам внутри одной категории
    """

    def __init__(self, category: "Category") -> None:
        """
        Начальная инициализация данных для итерации.
        :param category: Категория продуктов, по которой будет происходить итерация.
        """
        self.products = category.products
        self.index = 0

    def __iter__(self) -> Iterator[Product]:
        """
        Метод для получения итератора по объектам класса.
        :return:
        """
        return self

    def __next__(self) -> Product:
        """
        Метод для считывания следующего объекта класса.
        :return:
        """
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
