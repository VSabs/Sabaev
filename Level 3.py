# Задача 1 (Создание списка)
# Создай список fruits с тремя элементами: "apple", "banana" и "orange". Затем выведи его на экран.
from operator import index
from os import remove

fruits = ["apple", "banana", "orange"]


# Задача 2 (Добавление элементов в список)
# Дан список:
# numbers = [10, 20, 30]
# Добавь число 40 в конец списка, затем выведи обновлённый список.

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)


# Задача 3 (Получение элементов списка)
# Дан список:
# colors = ["red", "green", "blue", "yellow"]
# Выведи второй элемент этого списка (индексация начинается с 0).

colors = ["red", "green", "blue", "yellow"]
print(colors[1])


# Задача 4 (Срезы списка)
# Дан список:
# letters = ["a", "b", "c", "d", "e", "f"]
# Выведи срез с третьего по пятый элемент включительно.

letters = ["a", "b", "c", "d", "e", "f"]
print(letters[2:5])


# Задача 5 (Замена элементов в списке)
# Дан список:
# items = ["book", "pen", "pencil", "eraser"]
# Замени элемент "pencil" на "ruler", затем выведи обновлённый список.

items = ["book", "pen", "pencil", "eraser"]
items[2] = "ruler"
print(items)


# Задача 6 (Удаление элементов из списка)
# Дан список:
# animals = ["cat", "dog", "elephant", "giraffe"]
# Удали элемент "elephant" по значению (не по индексу), затем выведи список.

animals = ["cat", "dog", "elephant", "giraffe"]
animals.remove("elephant")
print(animals)


# Задача 7 (Слияние списков)
# Даны два списка:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Объедини их в один список (без изменения исходных) и выведи результат.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)


# Задача 8 (Добавление элемента в конкретное место списка)
# Дан список:
# numbers = [10, 20, 40, 50]
# Вставь число 30 между 20 и 40, затем выведи список.

numbers = [10, 20, 40, 50]
numbers.insert(2, 30)
print(numbers)


# Задача 9 (Очистка списка)
# Дан список:
# data = ["temp", "log", "backup", "cache"]
# Полностью очисти его, затем выведи пустой список.

data = ["temp", "log", "backup", "cache"]
data.clear()
print(data)

# Задача 1 (Добавление элементов в список)
# Дан список:
# python

numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(0,5)
print(numbers)

# Задача 2 (Срезы списка)
# Дан список:
# python

letters = ['a', 'b', 'c', 'd', 'e', 'f']
slice_1 = letters[2:5]
slice_2 = letters[::2]
print(slice_1)
print(slice_2)

# Задача 3 (Удаление элементов из списка)
# Дан список:
# python

colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
colors.remove("green")
colors.pop(3)
print(colors)

# Задача 4 (Слияние списков)
# Дан два списка:
# python

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

merged_list = list1 + list2
print(merged_list)

# Задача 5 (Замена элементов в списке)
# Дан список:
# python

items = [10, 20, 30, 40, 50]
index = items.index(30)
items[index] = "тридцать"
items[1] = 'двадцать'
print(items)












