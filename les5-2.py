"""Самостоятельно в переменной строку текста.
Создать словарь, где ключ - буква, значеие - код буквы."""

text_string = "Без труда не выловить и рыбку из пруда!"
print({key: ord(key) for key in set(text_string)})

