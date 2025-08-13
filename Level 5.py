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





