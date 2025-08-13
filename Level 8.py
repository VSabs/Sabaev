# Задача 1 (Создание и вызов функций)
# Напиши функцию greet(name), которая принимает имя (строка) и возвращает строку вида: "Привет, [name]!".
# Требования:
# Объяви функцию с одним параметром name
# используй f-строку для возврата результата

def greet(name):
    return f"Привет, {name}!"
print(greet("Анна"))

# Задача 2 (Аргументы с дефолтными значениями)
# Создай функцию make_coffee(), которая:
# Принимает 1 обязательный аргумент coffee_type (строка)
# И 1 необязательный аргумент sugar (число, по умолчанию 0)
# Возвращает строку вида:
# "Ваш [coffee_type] с [sugar] кусочками сахара"

def make_coffee(coffee_type, sugar = 0):
    return f"Ваш {coffee_type} с {sugar} кусочками сахара"


print(make_coffee("латте"))
print(make_coffee("капучино", 2))

# Упрощённая задача 3 (Возврат данных)
# Напиши функцию get_first_element(), которая:
# Принимает список любых элементов (например, ["яблоко", "банан", "вишня"])
# Возвращает первый элемент этого списка

def get_first_element(items):
    return items[0]


print(get_first_element([10, 20, 30]))
print(get_first_element(["а", "б", "в"]))

# Задача 1 (Функции в Python / Создание и вызов функций)
# Напиши функцию greet_user(), которая выводит в консоль сообщение "Привет, пользователь!". Затем вызови эту функцию дважды.

def greet_user():
    print("Привет, пользователь!")


greet_user()
greet_user()

# Задача 2 (Аргументы функций)
# Напиши функцию multiply(a, b), которая принимает два числа и возвращает их произведение. Вызови функцию с аргументами 3 и 5, затем выведи результат в консоль.

def multiply(a, b):
    return a * b


result = multiply(3, 5)
print(result)

# Задача 3 (Аргументы с дефолтными значениями)
# Напиши функцию welcome(name, greeting="Добро пожаловать"), которая принимает имя и опциональное приветствие (по умолчанию "Добро пожаловать"), затем возвращает строку в формате:
# "{greeting}, {name}!".
# Вызови функцию дважды:
# С одним аргументом — имя "Анна".
# С двумя аргументами — имя "Петр" и приветствие "Привет".

def welcome(name, greeting="Добро пожаловать"):
    return f"{greeting}, {name}"


print(welcome("Анна"))
print(welcome(name="Петр", greeting="Привет"))

# Задача 4 (Возвращение данных из функций)
# Напиши функцию is_even(num), которая принимает число и возвращает True, если оно чётное, и False — если нечётное. Вызови её с числами 4 и 7, затем выведи результаты в консоль.

def is_even(num):
    return num % 2 == 0


print(is_even(4))
print(is_even(7))

# Задача 5 (Декораторы)
# Напиши декоратор uppercase_decorator, который преобразует результат функции в верхний регистр.
# Примени его к функции say_hello(), возвращающей строку "hello".

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase_decorator
def say_hello():
    return "hello"

print(say_hello())

# Задача 1 (Функции в Python)
# Напиши функцию greet_user(), которая выводит в консоль строку "Привет, пользователь!".

def greet_user():
    print("Привет, пользователь!")


greet_user()

# Задача 2 (Аргументы функций)
# Напиши функцию multiply(a, b), которая принимает два числа и возвращает их произведение.
# Вызови функцию с аргументами 3 и 5, затем выведи результат в консоль.

def multiply(a, b):
    return a * b


print(multiply(3, 5))

# Задача 3 (Аргументы с дефолтными значениями)
# Напиши функцию create_message(name, greeting="Привет"), которая:
# Принимает имя (name) и опциональный аргумент greeting (значение по умолчанию: "Привет");
# Возвращает строку в формате "{greeting}, {name}!".

def create_message(name, greeting="Привет"):
    return f"{greeting}, {name}!"


print(create_message("Анна"))
print(create_message(name="Максим", greeting="Здравствуй"))

# Задача 4 (Возвращение данных из функций)
# Напиши функцию is_even(number), которая:
# Принимает целое число number;
# Возвращает True, если число чётное, и False — если нечётное.

def is_even(number):
    return number % 2 == 0


print(is_even(4))
print(is_even(7))

# Задача 5 (Декораторы)
# Напиши декоратор uppercase_decorator, который:
# Принимает функцию, возвращающую строку;
# Возвращает эту строку в верхнем регистре.

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase_decorator
def say_hello():
    return "hello"


print(say_hello())

# Задача 7 (Декораторы)
# Напиши декоратор add_exclamation, который добавляет восклицательный знак к результату функции. Пример:
# python
# @add_exclamation
# def greet():
#     return "Привет"
# print(greet())  # Должно вывести: "Привет!"

def add_exclamation(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper

@add_exclamation
def greet():
    return "Привет"


print(greet())  # Должно вывести: "Привет!"

# Задача 8 (Декораторы)
# Напиши декоратор repeat_twice, который вызывает функцию дважды и возвращает оба результата через пробел. Пример:
#
# python
# @repeat_twice
# def say_word():
#     return "Python"
#
# print(say_word())  # Должно вывести: "Python Python"

def repeat_twice(func):
    def wrapper():
        result = func()
        return f"{result} {result}"
    return wrapper


@repeat_twice
def say_word():
    return "Python"


print(say_word())  # Должно вывести: "Python Python"

# Задача 11 (Простой декоратор)
# Напиши декоратор make_uppercase, который преобразует результат функции в верхний регистр.
# python
# @make_uppercase
# def get_text():
#     return "hello world"
# print(get_text())  # Должно вывести: "HELLO WORLD"

def make_uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@make_uppercase
def get_text():
    return "hello world"


print(get_text())

# Задача 12 (Декоратор с замыканием)
# Напиши декоратор add_prefix, который добавляет слово "Уведомление:" к результату функции.
# @add_prefix
# def get_message():
#     return "Проверьте почту"
#
# print(get_message())  # Должно вывести: "Уведомление: Проверьте почту"

def add_prefix(func):
    def wrapper():
        result = func()
        return f"Уведомление: {result}"
    return wrapper


@add_prefix
def get_message():
    return "Проверьте почту"


print(get_message())

# Задача 14 (Лёгкий декоратор с аргументами функции)
# Напиши декоратор excited, который добавляет восклицательные знаки к результату функции. Количество знаков задаётся аргументом декоратора.
# python
# @excited(3)
# def say_hello():
#     return "Привет"
#
# print(say_hello())  # Должно вывести: "Привет!!!"

def excited(count):
    def decorator(func):
        def wrapper():
            result = func()
            return result + "!" * count
        return wrapper
    return decorator

@excited(3)
def say_hello():
    return "Привет"


print(say_hello())

# Задача 1 (Функции в Python)
# Напиши функцию greet_user(), которая выводит в консоль сообщение "Привет, пользователь!". Затем вызови эту функцию.

def greet_user():
    print("Привет, пользователь!")


greet_user()

# Задача 2 (Аргументы функций)
# Напиши функцию multiply(a, b), которая принимает два числа и возвращает их произведение. Вызови функцию с аргументами 3 и 5, а результат выведи в консоль.

def multiply(a, b):
    return a * b


print(multiply(3, 5))

# Задача 3 (Аргументы с дефолтными значениями)
# Напиши функцию welcome(name, greeting="Добро пожаловать"), которая принимает имя (name) и опциональный аргумент greeting (со значением по умолчанию). Функция должна возвращать строку в формате:
# "{greeting}, {name}!".

def welcome(name, greeting="Добро пожаловать"):
    return f"{greeting}, {name}!"


print(welcome("Анна"))
print(welcome(name="Максим", greeting="Привет"))

# Задача 4 (Возвращение данных из функций)
# Напиши функцию is_even(number), которая принимает целое число и возвращает True, если число чётное, и False — если нечётное. Вызови функцию с числами 4 и 7, а результаты выведи в консоль.

def is_even(number):
    return number % 2 == 0


print(is_even(4))
print(is_even(7))

# Задача 5 (Декораторы)
# Напиши декоратор uppercase_decorator, который преобразует результат декорируемой функции в верхний регистр.

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase_decorator
def say_hello():
    return "привет"


print(say_hello())

# Задача 1 (Дефолтные значения аргументов)
# Создай функцию greet(), которая принимает:
# Обязательный аргумент name (строка)
# Необязательный аргумент greeting (по умолчанию "Добрый день")
# Функция должна возвращать строку вида: "{greeting}, {name}!"

def greet(name, greeting="Добрый день"):
    return f"{greeting}, {name}"


print(greet("Анна"))
print(greet(name="Иван", greeting="Привет"))

# Задача 2 (Возвращение данных)
# Создай функцию calculate(), которая:
# Принимает два числа a и b
# Возвращает (не выводит!) сумму и произведение этих чисел в виде кортежа (сумма, произведение)
# Пример вызова:
# python
# result = calculate(3, 4)
# print(result)  # Должно вывести: (7, 12)

def calculate(a, b):
    return a + b, a * b


result = calculate(3, 4)
print(result)

# Задача 1 (Функции в Python)
# Напиши функцию greet_user(), которая принимает имя пользователя (строка) и выводит сообщение:
# "Привет, [имя]! Добро пожаловать!".
# Вызови эту функцию с аргументом "Анна".

def greet_user(name):
    print(f"Привет, {name}! Добро пожаловать!")


greet_user("Анна")
#
# Задача 2 (Аргументы функций)
# Напиши функцию multiply_numbers, которая принимает два числа и возвращает их произведение. Вызови функцию с аргументами 3 и 7, а результат выведи на экран через print.

def multiply_numbers(a, b):
    return a * b


print(multiply_numbers(3, 7))

# Задача 3 (Аргументы с дефолтными значениями)
# Напиши функцию make_coffee, которая принимает:
# Обязательный аргумент type (вид кофе, строка),
# Необязательный аргумент sugar (количество ложек сахара, int) со значением по умолчанию 1.
# Функция должна возвращать строку вида:
# "Кофе: [type], сахар: [sugar] ложек".
# Пример вызова:
# python
# print(make_coffee("латте"))  # Должно вернуть "Кофе: латте, сахар: 1 ложек"
# print(make_coffee("эспрессо", 3))  # Должно вернуть "Кофе: эспрессо, сахар: 3 ложек"

def make_coffee(type, sugar=1):
    return f"Кофе: {type}, сахар: {sugar} ложек"


print(make_coffee("латте"))
print(make_coffee("эспрессо", 3))

# Задача 4 (Возвращение данных из функций)
# Напиши функцию is_even, которая принимает число и возвращает True, если оно чётное, и False — если нечётное. Вызови функцию с числами 10 и 15, результаты выведи через print.

def is_even(a):
    return a % 2 == 0


print(is_even(10))
print(is_even(15))

# Задача 5 (Декораторы)
# Напиши декоратор repeat_twice, который заставляет функцию вызываться два раза. Пример использования:
# python
# @repeat_twice
# def say_hello():
#     print("Привет!")
# say_hello()
# Ожидаемый вывод:
# text
# Привет!
# Привет!

def repeat_twice(func):
    def wrapper():
        func()
        func()
    return wrapper


@repeat_twice
def say_hello():
    print("Привет!")


say_hello()

# Задача 6 (Функции в Python)
# Напиши функцию calculate_area(), которая:
# Принимает два аргумента (длину и ширину прямоугольника)
# Возвращает его площадь
# Если передан только один аргумент, считает площадь квадрата (длина = ширине)

def calculate_area(length, width=None):
    if width is None:
        return length * length
    return  length * width


print(calculate_area(3, 4))
print(calculate_area(5))


























