from src.classes import Category, Product   # pragma: no cover

if __name__ == "__main__": # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("1. Имя:", product1.name)
    print("1. Описание:", product1.description)
    print("1. Цена:", product1.price)
    print("1. Количество", product1.quantity)

    print("2. Имя:", product2.name)
    print("2. Описание:", product2.description)
    print("2. Цена:", product2.price)
    print("2. Количество", product2.quantity)

    print("3. Имя:", product3.name)
    print("3. Описание:", product3.description)
    print("3. Цена:", product3.price)
    print("3. Количество:", product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print("К1. Описание:", category1.description)
    print("К1. Длина списка:", len(category1.products))
    print("К1. К-во категорий:", category1.category_count)
    print("К1. К-во продуктов:", category1.product_count)
    print("К1. Всего продуктов:", category1.total_count)
    print("-----------")
    print("К1. Продукты:", category1.products)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print("К2. Имя:", category2.name)
    print("К2. Описание:", category2.description)
    print("К2. Длина списка:", len(category2.products))
    print("К2. Продукты:", category2.products)
    print("К2. Всего продуктов:", category2.total_count)

    print("Кол-во категорий в категориях:", Category.category_count)
    print("Кол-во продуктов в категориях:", Category.product_count)
