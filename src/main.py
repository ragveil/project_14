from src.classes import Category, LawnGrass, Smartphone  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print("Смартфон1. Название:", smartphone1.name)
    print("Смартфон1. Описание:", smartphone1.description)
    print("Смартфон1. Цена:", smartphone1.price)
    print("Смартфон1. Количество:", smartphone1.quantity)
    print("Смартфон1. Производительность:", smartphone1.efficiency)
    print("Смартфон1. Модель:", smartphone1.model)
    print("Смартфон1. Память:", smartphone1.memory)
    print("Смартфон1. Цвет:", smartphone1.color)

    print("Смартфон2. Название:", smartphone2.name)
    print("Смартфон2. Описание:", smartphone2.description)
    print("Смартфон2. Цена:", smartphone2.price)
    print("Смартфон2. Количество:", smartphone2.quantity)
    print("Смартфон2. Производительность:", smartphone2.efficiency)
    print("Смартфон2. Модель:", smartphone2.model)
    print("Смартфон2. Память:", smartphone2.memory)
    print("Смартфон2. Цвет:", smartphone2.color)

    print("Смартфон3. Название:", smartphone3.name)
    print("Смартфон3. Описание:", smartphone3.description)
    print("Смартфон3. Цена:", smartphone3.price)
    print("Смартфон3. Количество:", smartphone3.quantity)
    print("Смартфон3. Производительность:", smartphone3.efficiency)
    print("Смартфон3. Модель:", smartphone3.model)
    print("Смартфон3. Память:", smartphone3.memory)
    print("Смартфон3. Цвет:", smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print("Газонная трава1. Название:", grass1.name)
    print("Газонная трава1. Описание:", grass1.description)
    print("Газонная трава1. Цена:", grass1.price)
    print("Газонная трава1. Количество:", grass1.quantity)
    print("Газонная трава1. Страна-производитель:", grass1.country)
    print("Газонная трава1. Период всходов:", grass1.germination_period)
    print("Газонная трава1. Цвет:", grass1.color)

    print("Газонная трава2. Название:", grass2.name)
    print("Газонная трава2. Описание:", grass2.description)
    print("Газонная трава2. Цена:", grass2.price)
    print("Газонная трава2. Количество:", grass2.quantity)
    print("Газонная трава2. Страна-производитель:", grass2.country)
    print("Газонная трава2. Период всходов:", grass2.germination_period)
    print("Газонная трава2. Цвет:", grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print("Сумма смартфонов:", smartphone_sum)

    grass_sum = grass1 + grass2
    print("Сумма газонных трав:", grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Правильный вариант: Возникла ошибка TypeError при попытке сложения")
    else:
        print("Неправильный вариант: Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print("Продукты категории смартфонов:", category_smartphones.products)

    print("Количество уникальных продуктов в категории:", Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Правильный вариант: Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Неправильный вариант: Не возникла ошибка TypeError при добавлении не продукта")
