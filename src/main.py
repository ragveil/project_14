from src.classes import Category, MyException, Order, Product  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except MyException:
        print("Возникла ошибка ValueError, прерывающая работу программы при добавлении продукта с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())

    try:
        product5 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    except MyException as e:
        print(e)
        print("Нельзя добавить нулевое количество товара.")
    else:
        print(f"Товар {product5.name} был успешно добавлен в заказ.")
    finally:
        print("Обработка добавления товара завершена.")

    print("----------------")

    try:
        category_new = Category(
            "Проверка на ошибки", "Не знаю будет ли работать", [Product("Iphone 15", "512GB, Gray space", 210000.0, 0)]
        )
    except MyException as e:
        print(e)
        print("Нельзя добавить нулевое количество товара.")
    else:
        print(f"Товар {category_new.name} был успешно добавлен в заказ.")
    finally:
        print("Обработка добавления товара завершена.")

    print("----------------")

    try:
        ordered = Order(Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14), 0)
    except MyException as e:
        print(e)
        print("Нельзя добавить нулевое количество товара")
    else:
        print(f"Товар {ordered.name} был успешно добавлен в заказ.")
    finally:
        print("Обработка добавления товара завершена.")
