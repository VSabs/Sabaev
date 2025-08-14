# Задача 1 (Создание класса)
# Создай класс Book, который имеет:
# Атрибуты: title (название книги, строка) и author (автор, строка).
# Метод info(), который возвращает строку в формате: "Название: {title}, Автор: {author}".
# Пример вызова:
# python
# book = Book("1984", "Джордж Оруэлл")
# print(book.info())  # Должно вывести: "Название: 1984, Автор: Джордж Оруэлл"

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"Название: {self.title}, Автор: {self.author}"

book = Book("Властелин колец", "Роман Толкин")
print(book.info())

# Задача 2 (Методы класса + self)
# Создай класс Calculator, который имеет:
# Атрибут result (изначально равен 0).
# Метод add(self, num), который увеличивает result на num.
# Метод subtract(self, num), который уменьшает result на num.

class Calculator:
    def __init__(self, result=0 ):
        self.result = result

    def add(self, num):
        self.result += num


    def subtract(self, num):
        self.result -= num


calc = Calculator()
calc.add(5)
calc.subtract(3)
print(calc.result)

# Задача 3 (Конструктор класса и атрибуты)
# Создай класс Student с:
# Конструктором __init__, принимающим:
# name (строка)
# age (число)
# grade (число - класс обучения)
# Методом get_info(), который возвращает строку:
# "Студент: {name}, Возраст: {age}, Класс: {grade}"
# Пример:
# python
# student = Student("Анна", 15, 9)
# print(student.get_info())
# # Вывод: "Студент: Анна, Возраст: 15, Класс: 9"

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Студент: {self.name}, Возраст: {self.age}, Класс: {self.grade}"

student = Student("Анна", 15, 9)
print(student.get_info())

# Задача 4 (Классовые атрибуты)
# Создай класс School с:
# Классовым атрибутом school_name = "Моя школа"
# Конструктором, принимающим student_count (количество студентов)
# Методом info(), который возвращает:
# "Школа: {school_name}, Учеников: {student_count}"
# Пример:
# python
# school = School(200)
# print(school.info())
# # Вывод: "Школа: Моя школа, Учеников: 200"

class School:
    SCHOOL_NAME = "Моя школа"

    def __init__(self, student_count):
        self.student_count = student_count


    def info(self):
        return f"Школа: {self.SCHOOL_NAME}, Учеников: {self.student_count}"

school = School(200)
print(school.info())

# Задача 5 (Понимание self)
# Создай класс Counter с:
# Атрибутом count (начальное значение 0)
# Методом increment(), который увеличивает count на 1
# Методом show(), который возвращает текущее значение count
# Пример:
# python
# c = Counter()
# c.increment()
# c.increment()
# print(c.show())  # Должно вывести: 2

class Counter:

    def __init__(self, count=0):
        self.count = count

    def increment(self):
        self.count += 1

    def show(self):
        return self.count

c = Counter()
c.increment()
c.increment()
print(c.show())

# Задача 6 (Комбинированная: атрибуты + методы)
# Создай класс BankAccount с:
# Атрибутами:
# owner (владелец, строка)
# balance (баланс, число, начальное значение 0)
# Методами:
# deposit(amount) - пополняет баланс
# withdraw(amount) - снимает деньги (если средств достаточно)
# get_balance() - возвращает строку:
# "Владелец: {owner}, Баланс: {balance}"

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return f"Владелец: {self.owner}, Баланс: {self.balance}"

acc = BankAccount("Иван Петров")
acc.deposit(100)
acc.withdraw(30)
print(acc.get_balance())

# Задача 1 (Создание класса)
# Создай класс Box, который имеет:
# Атрибуты: width (ширина) и height (высота), задаваемые при создании объекта
# Метод area(), возвращающий площадь (width * height)
# Пример вызова:
# python
# box = Box(10, 20)
# print(box.area())  # Должно вывести 200

class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


box = Box(10, 20)
print(box.area())

# Задача 2 (Методы класса)
# Создай класс Counter с:
# Атрибутом count (начальное значение 0)
# Методом increment(), увеличивающим count на 1
# Методом reset(), обнуляющим count
# Пример:
# python
# c = Counter()
# c.increment()
# print(c.count)  # 1
# c.increment()
# print(c.count)  # 2
# c.reset()
# print(c.count)  # 0

class Counter:
    def __init__(self, count=0):
        self.count = count

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

c = Counter()
c.increment()
print(c.count)
c.increment()
print(c.count)
c.reset()
print(c.count)

# Задача 3 (Общие атрибуты)
# Создай класс Player с:
# Общим для всех объектов атрибутом game_name = "Chess" (название игры)
# Индивидуальным атрибутом name (имя игрока, задаётся при создании)
# Методом info(), возвращающим:
# "{name} играет в {game_name}"
# Пример:
# python
# p1 = Player("Анна")
# p2 = Player("Петр")
# print(p1.info())  # "Анна играет в Chess"
# print(p2.info())  # "Петр играет в Chess"

class Player:
    GAME_NAME = "Chess"

    def __init__(self, name):
        self.name = name

    def info(self):
        return f"{self.name} играет в {self.GAME_NAME}"

player1 = Player("Анна")
player2 = Player("Петр")
print(player1.info())
print(player2.info())

# Задача 4 (Понимание self)
# Создай класс LightBulb с:
# Атрибутом is_on (начальное значение False)
# Методом switch(), который:
# Меняет состояние is_on на противоположное (если было True → False, и наоборот)
# Возвращает строку "Лампа включена" или "Лампа выключена" в зависимости от состояния
# Пример:
# python
# bulb = LightBulb()
# print(bulb.switch())  # "Лампа включена"
# print(bulb.switch())  # "Лампа выключена"

class LightBuld:
    def __init__(self):
        self.is_on = False

    def switch(self):
        self.is_on = not self.is_on
        return "Лампа включена" if self.is_on else "Лампа выключена"

buld = LightBuld()
print(buld.switch())
print(buld.switch())

# Задача 1 (Методы класса)
# Создай класс Calculator. Добавь в него метод add, который принимает два числа и возвращает их сумму.
# Вызов метода должен выглядеть так:
# python
# calc = Calculator()
# result = calc.add(3, 5)
# print(result)  # Должно вывести 8

class Calculator:

    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(3, 5)
print(result)
#
# Задача 2 (Конструктор класса __init__)
# Создай класс Book. В конструкторе (__init__) инициализируй атрибуты:
# title — название книги (строка),
# author — автор книги (строка),
# pages — количество страниц (целое число).
# После создания объекта выведи его атрибуты.
# Пример использования:
# python
# book = Book("1984", "George Orwell", 328)
# print(book.title)   # Должно вывести "1984"
# print(book.author)  # Должно вывести "George Orwell"
# print(book.pages)   # Должно вывести 328

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book = Book("1984", "George Orwell", 328 )
print(book.title)
print(book.author)
print(book.pages)

# Задача 3 (Общие атрибуты класса)
# Создай класс SpaceShip с общим для всех объектов атрибутом fuel_type = "термоядерное". Добавь в конструктор индивидуальные атрибуты:
# name - название корабля (строка)
# crew - количество экипажа (целое число)
# Создай два разных корабля и проверь общий атрибут.
# Пример использования:
# python
# ship1 = SpaceShip("Аполлон", 5)
# ship2 = SpaceShip("Созвездие", 3)
# print(ship1.fuel_type)  # Должно вывести "термоядерное"
# print(ship2.fuel_type)  # Должно вывести "термоядерное"
# print(ship1.name)      # Должно вывести "Аполлон"

class SpaceShip:

    FUEL_TYPE = "термоядерное"

    def __init__(self, name, crew):
        self.name = name
        self.crew = crew

ship = SpaceShip("Союз", 5)
ship2 = SpaceShip("Ракета", 3)

print(ship.FUEL_TYPE)
print(ship2.FUEL_TYPE)
print(ship.name)

# Задача 4 (Параметр self)
# Создай класс Robot с методом introduce(), который выводит сообщение с именем робота. Имя должно передаваться при создании объекта.
# Пример использования:
# python
# r2d2 = Robot("R2-D2")
# r2d2.introduce()  # Должно вывести: "Я робот. Меня зовут R2-D2"
# c3po = Robot("C-3PO")
# c3po.introduce()  # Должно вывести: "Я робот. Меня зовут C-3PO"

class Robot:

    def __init__(self, name):
        self.name = name


    def introduce(self):
        print( f"Я робот. Меня зовут {self.name}")

r2d2 = Robot("R2-D2")
r2d2.introduce()

c3po = Robot("C-3PO")
c3po.introduce()

# Задача 5 (Работа с методами класса)
# Создай класс BankAccount с методами:
# __init__ - инициализирует атрибут balance (начальный баланс, по умолчанию 0)
# deposit - увеличивает баланс на указанную сумму
# withdraw - уменьшает баланс на указанную сумму (если средств хватает)
# check_balance - выводит текущий баланс
# Пример использования:
# python
# account = BankAccount()
# account.deposit(1000)
# account.withdraw(300)
# account.check_balance()  # Должно вывести: 700

class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
                self.balance -= amount
        else:
            print("Недостаточно средств")

    def check_balance(self):
        print(f"Текущий баланс: {self.balance}")

account = BankAccount()
account.deposit(1000)
account.withdraw(300)
account.check_balance()

# Задача 1 (Конструктор класса __init__ и атрибуты)
# Создай класс Book:
# С конструктором, принимающим 3 параметра: title (название), author (автор), pages (количество страниц)
# Инициализируй эти параметры как атрибуты объекта
# Добавь метод describe(), который возвращает строку: "[Название] by [Автор], [Страницы] pages"
# Проверь работу:
# Создай объект Book("Python Basics", "A. Smith", 200)
# Вызови describe() и выведи результат

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"{self.title} by {self.author}, {self.pages}"


my_book = Book("Моя книга", "Сабаев", 41)
print(my_book.describe())

# Первая задача (№1 — Конструктор класса):
# Создай класс Robot с конструктором __init__(), который принимает параметр name и сохраняет его в атрибут экземпляра. Добавь метод greet(), выводящий "Hello, I'm {name}".
# Проверь работу: создай экземпляр Robot с именем "R2-D2" и вызови greet().
# Что нужно сделать:
# Напиши класс с __init__ и методом
# Создай объект и вызови метод

class Robot:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")


my_robot = Robot("R2-D2")
my_robot.greet()

# Следующая задача (№2 - Атрибуты класса и экземпляра):
# Создай класс Spaceship:
# С общим атрибутом класса fuel_type = "антиматерия"
# С конструктором, принимающим model (сохраняет в атрибут экземпляра)
# С методом info(), выводящим: "Модель: {model}, Топливо: {fuel_type}"
# Проверь: создай экземпляр Spaceship("USS Enterprise") и вызови info().

class Spaceship:

    FUEL_TYPE = "антиматерия"

    def __init__(self, model):
        self.model = model

    def info(self):
        print(f"Модель: {self.model}, Топливо: {self.FUEL_TYPE}")


my_spaceship = Spaceship("USS Enterprise")
my_spaceship.info()

# Следующая задача (№3 - Работа с объектами):
# Создай класс BankAccount:
# С конструктором, принимающим account_holder (владелец) и balance (баланс, по умолчанию 0)
# С методами:
# deposit(amount) - увеличивает баланс
# withdraw(amount) - уменьшает баланс (нельзя уйти в минус!)
# check_balance() - возвращает строку: "{account_holder}, баланс: {balance}₽"
# Проверь: создай аккаунт, внеси 1000₽, сними 500₽ и проверь баланс.

class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств")

    def check_balance(self):
        return f"{self.account_holder}, баланс: {self.balance}₽"


my_account = BankAccount("Вертолек", 500)
my_account.deposit(1000)
my_account.withdraw(300)
print(my_account.check_balance())




















