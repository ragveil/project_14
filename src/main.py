from src.classes import Category, Product   # pragma: no cover

if __name__ == "__main__": # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    print("Описание первого продукта:", product1.description)
    print("Название второго продукта:", product2.name)
    print("Цена третьего продукта:", product3.price)
    print("Продукты первой категории:", category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("Продукты первой категории:", category1.products)
    print("Число моделей в первой категории:", category1.product_count)
    print("Всего продуктов в первой категории:", category1.total_count)
    print("Список продуктов в соответствии с ТЗ:", category1.products_list)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 1180000.0,
            "quantity": 15,
        },
        category1,
    )
    print("Название нового продукта:", new_product.name)
    print("Описание нового продукта:", new_product.description)
    print("Цена нового продукта:", new_product.price)
    print("Количество нового продукта:", new_product.quantity)
    new_product.price = 800
    print("Новая цена продукта:", new_product.price)

    new_product.price = -100
    print("Новая цена продукта (отрицательная):", new_product.price)
    new_product.price = 0
    print("Новая цена продукта (нулевая):", new_product.price)
    print(new_product)
