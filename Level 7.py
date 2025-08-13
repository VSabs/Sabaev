# Задача 1 (Работа с файлами)
# Создай новый файл greeting.txt и запиши в него строку: "Hello, Python!".
# Требования:
# Используй метод write()
# Не забудь закрыть файл после записи
#
file = open("greeting.txt", "w", encoding="UTF-8")
file.write("Hello, Python!")
file.close()

# Задача 2 (Контекстный менеджер with)
# Прочитай содержимое файла greeting.txt (который ты создал в предыдущей задаче) и выведи его на экран, используя конструкцию with.

with open("greeting.txt", "r", encoding="UTF-8") as file:
    print(file.read())

# Задача 3 (Добавление в файл)
# Добавь строку "\nI'm learning file operations!" в конец файла greeting.txt, сохранив его предыдущее содержимое.
# Требования:
# Используй режим добавления ("a" или "a+")
# Примени контекстный менеджер with
# Убедись, что новая строка начинается с переноса (\n)

with open("greeting.txt", "a", encoding="UTF-8") as file:
    file.write("\nI'm learning file operations!")

# Задача 4 (Комбинированные операции с файлами)
# Прочитай содержимое файла greeting.txt, добавь в конец строку "\nThis is awesome!", а затем выведи обновлённое содержимое файла на экран.
# Требования:
# Используй режим "r+" для чтения и записи
# Примени методы:
# .read() для чтения
# .seek() для перемещения курсора в конец файла
# .write() для добавления текста

with open("greeting.txt", "r+", encoding="UTF-8") as file:
    file_save = file.read()
    file.seek(0, 2)
    print(file_save + "\nThis is awesome!")






























