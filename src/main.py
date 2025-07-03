from src.classes import Category, Order, Product  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("Продукт1, Название:", product1.name)
    print("Продукт1, Описание:", product1.description)
    print("Продукт1, Цена:", product1.price)
    print("Продукт1, Количество:", product1.quantity)

    print("Продукт2, Название:", product2.name)
    print("Продукт2, Описание:", product2.description)
    print("Продукт2, Цена:", product2.price)
    print("Продукт2, Количество:", product2.quantity)

    print("Продукт3, Название:", product3.name)
    print("Продукт3, Описание:", product3.description)
    print("Продукт3, Цена:", product3.price)
    print("Продукт3, Количество:", product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print("Категория1, Название:", category1.name == "Смартфоны")
    print("Категория1, Описание:", category1.description)
    print("Категория1, Количество продуктов:", len(category1.products))
    print("Категория1, Количество категорий:", category1.category_count)
    print("Категория1, Количество продуктов:", category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print("Категория2, Название:", category2.name)
    print("Категория2, Описание:", category2.description)
    print("Категория2, Количество продуктов:", len(category2.products))
    print("Категория2, Продукты:", category2.products)

    print("Количество категорий:", Category.category_count)
    print("Количество продуктов:", Category.product_count)

    order1 = Order(product1, 5)
    order2 = Order(product2, 8)
    order3 = Order(product3, 15)

    print(order1)
    print(order2)
    print(order3)
