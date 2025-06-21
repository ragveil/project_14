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
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории.
    """

    products: list[Product]
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Метод для инициализации экземпляра класса категории.
        :param name: Наименование категории, str.
        :param description: Описание категории, str.
        :param products: Список продуктов, list[Product].
        """
        self.name = name
        self.description = description
        self.products = products
        self.total_count = sum(Product.quantity for Product in products)
        Category.product_count += len(products)
        Category.category_count += 1
