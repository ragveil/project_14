## Описание проекта
Разработка ядра для интернет-магазина в рамках домашней работы.

## Установка
1. Клонирование репозитория
```
https://github.com/ragveil/project_14
```
2. Установка зависимостей
```
poetry install
```
## Обновления
На данном этапе работы ведется более глубока разработка классового функционала.
Аттрибуты цены для класса `Products` и продукты категории для класса `Category` теперь являются приватными.
Созданы методы для взаимодействия с приватными аттрибутами классов.

---
## Модуль `main.py`
На данном этапе модуль служит для проверки работу реализованных функций.

---
## Модуль `classes.py`
Модуль `classes.py` содержит данные о классах `Product` и `Category`

---
## Модуль `json_reader.py`
Модуль `json_reader.py` содержит функцию `get_class_obj()` для выгрузки данных из JSON-файла и инициализации этих данных в классы.

### Пример работы модуля `json_reader.py`
```python
from src.constants import PATH_TO_JSON
from src.json_reader import get_class_obj

path = PATH_TO_JSON
products, categories = get_class_obj(path)
product1, product2, product3, product4 = products
category1, category2 = categories

print(product1.name, product1.price) # Результат: Samsung Galaxy S23 Ultra, 180000.0
print(category1.total_count) # Результат: 27

```
