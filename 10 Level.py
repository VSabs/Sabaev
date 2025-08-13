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















