from typing import Optional


class Product:
    """
    Класс для представления продукта.
    """

    name: str
    description: str
    price: float
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

    def __repr__(self):
        return f'{self.name}, {self.price} руб., Остаток: {self.quantity} шт.'

    @classmethod
    def new_product(cls, prod_dict: dict):
        products = Category.products
        if prod_dict.keys() == {'name', 'description', 'price', 'quantity'}:
            name, description, price, quantity = prod_dict.values()
            for item in products:
                if item.name == name:
                    item.quantity += quantity
                    item.price = max(price, item.price)
                else:
                    return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print(f'Указанное значение ниже или равно нулю.')
        elif new_price < self.price:
            answer = input('Указанная цена ниже уже установленной. Введите "Y", чтобы подтвердить изменение цены.')
            if answer.lower() == 'y':
                self.__price = new_price
            else:
                print(f'Цена осталась без изменений - {self.__price}.')

    # def __str__(self):
    #     return Product.__str__(self)
    # def __repr__(self):
    #     return Product.__repr__(self)


class Category:
    """
    Класс для представления категории.
    """
    product_count: int = 0
    category_count: int = 0


    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None):
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

    def add_product(self, product: Product):
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
