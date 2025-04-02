"""Продолжить задачу 2.
Сохранить словарь в итераторвю
Вывести пар значений и ключей."""
import sys
text_string = "Без труда не выловить и рыбку из пруда!"
d = ({key: ord(key) for key in set(text_string)})
iterator = iter(d.items())
print(iterator, type(iterator), sys.getsizeof(iterator), sys.getsizeof(d))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print()
for i in iterator:
    print(i)