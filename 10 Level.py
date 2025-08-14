# Задача 1 (Наследование, базовый синтаксис)
# Создай:
# Родительский класс Vehicle с методом start_engine() (пусть выводит "Engine started").
# Дочерний класс Car, который наследует Vehicle и переопределяет start_engine(), добавляя к исходному сообщению ", car is ready!" (итог: "Engine started, car is ready!").
# Проверь работу, создав объект Car и вызвав его метод.

class Vehicle:

    def start_engine(self):
        return f"Engine started"


class Car(Vehicle):

    def start_engine(self):
        parament_message = super().start_engine()
        return  parament_message + ", car is ready!"


my_car = Car()
print(my_car.start_engine())

# Задача 2 (Наследование — расширение функционала)
# Создай:
# Родительский класс Device с методом turn_on() (пусть выводит "Device is turned on").
# Дочерний класс Smartphone, который:
# Наследует Device
# Добавляет новый метод unlock() (выводит "Screen unlocked")
# Не переопределяет turn_on()
# Проверь работу:
# Создай объект Smartphone
# Вызови оба метода (turn_on() и unlock())

class Device:

    def turn_on(self):
        print("Device is turned on")


class Smartphone(Device):

    def unlock(self):
        print("Screen unlocked")


my_phone = Smartphone()
my_phone.unlock()
my_phone.turn_on()

# Задача 3 (Многоуровневое наследование)
# Создай иерархию классов:
# Базовый класс Animal с методом eat() (выводит "Eating...")
# Дочерний класс Dog (наследует Animal), добавляет метод bark() ("Woof!")
# Класс Puppy (наследует Dog), переопределяет bark() ("Yip-yip!")
# Проверь:
# Создай объект Puppy
# Вызови все доступные методы (eat() и bark())

class Animal:

    def eat(self):
        print("Eating...")


class Dog(Animal):

    def bark(self):
        print("Woof!")


class Puppy(Dog):

    def bark(self):
        print("Yip-yip!")


my_puppy = Puppy()
my_puppy.eat()
my_puppy.bark()

# Задача 1 (Базовое наследование)
# Создай класс Animal с методом make_sound(), который печатает "Some generic sound". Затем создай класс Dog, который наследуется от Animal и переопределяет метод make_sound(), чтобы он печатал "Woof!".
#
# Проверь работу, создав экземпляр Dog и вызвав его метод.

class Animal:

    def make_sound(self):
        print("Some generic sound")


class Dog(Animal):

    def make_sound(self):
        print("Woof!")

my_dog = Dog()
my_dog.make_sound()

# Задача 2 (Использование super())
# Создай класс Vehicle с методом __init__(), который принимает max_speed и сохраняет его в атрибут. Затем создай класс Car, который наследуется от Vehicle и добавляет атрибут brand. В Car.__init__() используй super(), чтобы не дублировать код инициализации max_speed.
#
# Проверь работу, создав экземпляр Car с параметрами max_speed=200 и brand="Toyota", затем выведи его атрибуты.

class Vehicle:

    def __init__(self, max_speed):
        self.max_speed = max_speed


class Car(Vehicle):

    def __init__(self, max_speed, brand):
     super().__init__(max_speed)
     self.brand = brand


my_cars = Car(max_speed=200, brand="Toyota")
print(my_cars.max_speed)
print(my_cars.brand)

# Первая задача (№1):
# Создай класс Book с методом describe(), который печатает "This is a book". Затем создай класс Novel, который наследуется от Book и переопределяет describe(), чтобы он печатал "This is a novel".
# Проверь работу, создав экземпляр Novel и вызвав его метод.

class Book:

    def describe(self):
        print("This is a book")


class Novel(Book):
    def describe(self):
        print("This is a novel")


my_book = Novel()
my_book.describe()

# Задача 2 (Использование super())
# Создай класс Device с методом __init__(), который принимает параметр power (мощность) и сохраняет его в атрибут.
# Затем создай класс SmartDevice, который:
# Наследуется от Device
# В своем __init__() принимает два параметра: power и os (операционная система)
# Использует super() для вызова __init__() родительского класса с параметром power
# Сохраняет os в отдельный атрибут
# Проверь работу, создав экземпляр SmartDevice с параметрами power=100 и os="Android", затем выведи оба его атрибута.

class Device:

    def __init__(self, power):
        self.power = power


class SmartDevice(Device):

    def __init__(self, power, os):
        super().__init__(power)
        self.os = os


my_device = SmartDevice(power=100, os="Android")
print(my_device.power)
print(my_device.os)

# Следующая задача (№3): Добавление новых методов
# Создай класс Employee с методом work(), который печатает "I'm working". Затем создай класс Manager, который:
# Наследуется от Employee
# Добавляет новый метод manage() с выводом "I'm managing"
# Переопределяет work() для вывода "I'm working hard!"
# Проверь работу, создав экземпляр Manager и вызвав оба метода.

class Employee:

    def work(self):
        print("I'm working")


class Manager(Employee):

    def manage(self):
        print("I'm managing")

    def work(self):
        print("I'm working hard!")


my_manager = Manager()
my_manager.manage()
my_manager.work()

# Следующая задача (№4): Множественное наследование
# Создай:
# Класс Camera с методом take_photo() (выводит "Photo taken")
# Класс Phone с методом make_call() (выводит "Calling...")
# Класс Smartphone, который наследуется от обоих классов и добавляет метод play_game() (выводит "Playing game")
# Проверь работу, создав экземпляр Smartphone и вызвав все три метода.

class Camera:

    def take_photo(self):
        print("Photo taken")


class Phone:

    def make_call(self):
        print("Calling...")


class Smartphone(Camera, Phone):

    def play_game(self):
        print("Playing game")


my_smartphone = Smartphone()
my_smartphone.play_game()
my_smartphone.make_call()
my_smartphone.take_photo()










































