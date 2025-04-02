"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""


def return_tuple(path):
    """Функция принимает путь и возвращает кортеж вида (путь, имя файла, расширение)."""
    *a, file_name = path.split('\\') #достаем имя файла, экранируем символ "\"
    name, extension = file_name.split(".")
    return path, file_name, extension

path1 = "C:\Thecode\Media\статья.txt"
path2 = "C:\julia\PycharmProjects\Geekbrains\.venv\Scripts\python.exe"
print(return_tuple(path1))
print(return_tuple(path2))

