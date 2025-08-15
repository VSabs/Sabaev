# Задача 1 (Создание словаря)
# Создай словарь student с ключами:
#
# "name" (значение — твоё имя, например "Алекс"),
#
# "age" (значение — твой возраст, например 20),
#
# "course" (значение — "Python").

student = {
    "name": "Виталий",
    "age": 29,
    "course": "Python"
}
print(student)
#
# Задача 2 (Доступ к элементам по ключу)
# Дан словарь:

car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(car["model"])
#
# Задача 3 (Добавление элемента в словарь)
# Дан словарь:

book = {
    "title": "1984",
    "author": "Оруэлл"
}

book["year"] = 1949
print(book)

# Задача 4 (Обновление значения по ключу)
# Дан словарь:

phone = {"brand": "Samsung", "model": "Galaxy S21", "year": 2021}
# Измени значение ключа "year" на 2022.
phone["year"] = 2022
print(phone)

# Задача 5 (Удаление элемента по ключу)
# Дан словарь:

laptop = {"brand": "Lenovo", "model": "ThinkPad", "year": 2020, "price": 1500}
# Удали ключ "price" и его значение.
del laptop["price"]
print(laptop)

# Задача 6 (Метод .get() и проверка ключа)
# Дан словарь:

colors = {"red": "красный", "blue": "синий", "green": "зеленый"}
# # Получи значение для ключа "blue" с помощью метода .get().
# #
# # Проверь, есть ли ключ "yellow" в словаре (выведи True или False).
#
print(colors.get("blue"))
if "yellow" in colors:
    print(True)
else:
    print(False)

# Задача 7 (Методы .keys(), .values(), .items())
# Дан словарь:

country = {"name": "Япония", "capital": "Токио", "population": 126_500_000}

print(country.keys())
print(country.values())
print(country.items())

# Задача 8 (Объединение словарей)
# Дан словарь:

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Объедини их в один словарь dict3 (используй метод update() или оператор | в Python 3.9+).

dict3 = dict1 | dict2
print(dict3)

# Первая задача (№1 — создание словаря):
# Создай словарь student с ключами:
# "name" (значение — твоё имя)
# "age" (твой возраст)
# "courses" (список из 2-3 предметов, например ["математика", "физика"])
# Выведи словарь через print().

student = {
    "name": "Виталий",
    "age": 29,
    "courses": ["математика", "физика"]
}
print(student)

# Следующая задача (№2 — доступ по ключу):
# Дан словарь:
# python
car = {"brand": "Toyota", "model": "Camry", "year": 2020}
print(car["brand"], car["year"])

# Следующая задача (№3 — добавление/обновление элементов):
# Дан словарь:
# python
# phone = {"brand": "Samsung", "model": "Galaxy"}
# Добавь в него:
# Новый ключ "year" со значением 2022
# Обнови "model" на "Galaxy S23"

phone = {
    "brand": "Samsung",
    "model": "Galaxy"
}
phone["year"] = 2022
phone["model"] = "Galaxy S23"
print(phone)

# Следующая задача (№4 — удаление элементов):
# Дан словарь:
# python

laptop = {"brand": "Lenovo", "model": "ThinkPad", "year": 2021, "price": 1500}
laptop.pop("price")
print(laptop)

# Следующая задача (№5 — методы словарей):
# Дан словарь:
#
# python

book = {"title": "1984", "author": "Оруэлл", "year": 1949}
print(list (book.keys()))
print(list (book.values()))

# Следующая задача (№6 — проверка элементов):
# Дан словарь:
# python

user = {"name": "Анна", "age": 25, "email": "anna@example.com"}
print("email" in user)
print( 25 in user.values())











