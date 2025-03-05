from sys import getsizeof
from typing import Hashable
data = [1, "jsjks", 5.11, [1, 2, 3], 5.11]
for i, value in enumerate(data):
    print(i, value, id(value), getsizeof(value), end = ' ')
    if isinstance(value, Hashable):
        print(hash(value))
    if isinstance(value, int):
        print("целое")
    if isinstance(value, str):
        print('строка')
